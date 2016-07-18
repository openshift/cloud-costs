// <![CDATA[
$(document).ready(function() {
    // dataTable.each()
    $('table.datatable').each(function(idx) {
        var this_id = $(this).attr('id');
        // main dataTable definition
        var table = $(this).DataTable({
            "processing" : true,
            "serverSide" : false,
            "paging" : true,
            "pageLength" : 10,
            "autoWidth" : false,
            "ajax" : {
                "url" : "data",
                "type" : "GET",
            },
            // columns need to map to HTML table
            "columns" : [
                {
                    'data' : null,
                    'className' : 'details-control',
                    'orderable' : false,
                    'defaultContent' : ''
                },
                { 'data' : 'zone', 'className' : 'availability-zone' },
                { 'data' : 'type', 'className' : 'instance-type' },
                {
                    'data' : 'running',
                    'className' : 'running-count',
                    'render' : function (data, type, full, meta) {
                        return '<a href="#" class="running-count-link">'+data+'</a>';
                    }
                },
                { 'data' : 'reserved', 'className' : 'reservation-count' },
                { 'data' : 'delta', 'className' : 'delta-col' },
                { 'data' : 'upfront', 'className' : 'upfront-col' },
                { 'data' : 'savings', 'className' : 'savings-col' },
                {
                    'data' : null,
                    'className' : 'purchase-control',
                    'orderable' : false,
                    'defaultContent' : '<p class="purchase-button">Purchase</p>'
                },
            ],
            "order": [[5, 'asc']],
            "rowCallback" : function (row, data, index) {
                var className = "";
                if (parseInt(data.delta) > 0) {
                    className = 'positive';
                } else if (parseInt(data.delta) < 0) {
                    className = 'negative';
                }
                $('td:eq(5)', row).addClass(className);

                var savings = Number(data.savings.replace(/[^0-9\.-]+/g,""));
                if (savings > 0) {
                    className = 'positive';
                } else if (savings < 0) {
                    className = 'negative';
                }
                $('td:eq(7)', row).addClass(className);

                return row;
            },
            "footerCallback" : function (row, data, start, end, display) {
                var api = this.api(), data;

                cols = [3,4,5,6]
                for (n in cols) {
                    // Total over all pages
                    total = api
                    .column( cols[n] )
                    .data()
                    .reduce( function (a, b) {
                        a = String(a).replace(/[^0-9\.-]+/g,"")
                        b = String(b).replace(/[^0-9\.-]+/g,"")
                        return Number(a) + Number(b);
                    }, 0 );

                    // because the table renders itself a couple times,
                    // to preserve the label, we need to strip out
                    // previous iterations of the total.
                    var label = $(api.column(cols[n]).footer()).html().replace(/\(-?\$?\d+,?\d*\.?\d*\)/,'');
                    // Update footer
                    if (cols[n] == 6) {
                        $(api.column(cols[n]).footer()).html(
                            label + ' ('+
                            total.toLocaleString(
                                'en-US', {
                                    style : 'currency',
                                    currency : 'USD',
                                    currencyDisplay : 'symbol',
                                    minimumFractionDigits : 2
                            })+
                            ')'
                        );
                    } else {
                        $( api.column( cols[n] ).footer() ).html(
                            label+' ('+total +')'
                        );
                    }
                }
            },
            'buttons' : [{ text : 'RI Graph',
                            action : function (e,dt,node,config) {
                                // Reservation expiration Dialog
                                var dialog = $("#dialog").dialog({
                                        autoOpen: false,
                                        height: 'auto',
                                        width: 'auto',
                                        modal: false,
                                        resizable: true,
                                        closeOnEscape: true,
                                        closeText: null,
                                });
                                var account = this_id;
                                console.log(account);
                                dialog.dialog("open").html("<div id='chart'>Loading...</div>");
                                $.ajax({
                                    type: 'GET',
                                    url: '/reservation/expiration-graph',
                                    data: {},
                                    dataType: "html",
                                    success: function(data) {
                                        $("#dialog")
                                            .html("<div id='chart'><svg id='d3-svg'/></div>"+data)
                                            .dialog({ title: 'RI Expiration' })
                                    }
                                })
                            }},
                            { text : 'Reload',
                                action: function() {
                                    table.ajax.reload();
                            }}
                    ],
            'dom' : '<"fg-toolbar ui-toolbar ui-widget-header ui-helper-clearfix ui-corner-tl ui-corner-tr"Blfr>'+
            't'+
            '<"fg-toolbar ui-toolbar ui-widget-header ui-helper-clearfix ui-corner-bl ui-corner-br"ip>',
        }) // end DataTable

        // Add event listener for opening and closing details
        $('table.datatable#'+$(this).attr("id")+' tbody').on('click', 'td.details-control', function () {
            var tr = $(this).closest('tr');
            var row = table.row( tr );

            if ( row.child.isShown() ) {
                // This row is already open - close it
                row.child.hide();
                tr.removeClass('shown');
            } else {
                // Open this row
                row.child( format_details(row.data()) ).show();
                tr.addClass('shown');
            }
        } );

        // Instances List Dialog
        var dialog = $("#dialog").dialog({
                autoOpen: false,
                height: 'auto',
                width: 'auto',
                modal: false,
                resizable: true,
                closeOnEscape: true,
                closeText: null,
        });

        // Add event listener for displaying instances list dialog
        $('table.datatable#'+$(this).attr("id")+' tbody').on('click', 'a.running-count-link', function () {
            var row = $(this).closest("tr");
            var account = $(this).closest("table.results_table").attr('id');
            var az = row.children("td.availability-zone").text();
            var size = row.children("td.instance-type").text();

            var tbl = '<table class="instances-table"></table>';
            $("#dialog").html(tbl)
                .children('table.instances-table')
                .DataTable({
                    "processing" : true,
                    "serverSide" : false,
                    "paging" : true,
                    "pageLength" : 10,
                    "autoWidth" : false,
                    "ajax" : {
                        "url": '/reservation/instances',
                        "type" : "POST",
                        "data": {
                            'availability-zone' : az,
                            'instance-type' :  size,
                            'account' : account
                        },
                    },
                    "columns" : [
                        {
                            'data' : 'id',
                            'className' : 'instances-id-col',
                            'title' : 'ID',
                        },
                        {
                            'data' : 'account',
                            'className' : 'instances-account-col',
                            'title' : 'Account',
                        },
                        {
                            'data' : 'name',
                            'className' : 'instances-name-col',
                            'title' : 'Name',
                        },
                        {
                            'data' : 'env',
                            'className' : 'instances-env-col',
                            'title' : 'Environment',
                        },
                    ]
                });
            $("#dialog")
                .dialog({ title: size+' in '+az })
                .dialog("open");
        });

        // Add event listener for purchases dialog
        $('table.datatable#'+$(this).attr("id")+' tbody').on('click', 'td.purchase-control', function () {
            var row = $(this).closest("tr");
            var account = $(this).closest("table.results_table").attr('id');
            var az = row.children("td.availability-zone").text();
            var size = row.children("td.instance-type").text();
            var delta = Math.abs(Number(row.children("td.delta-col").text()));

            console.log()
            var tbl = '<form class="purchase-form" method="post">' +
                        'Account: ' + '<input type="text" name="account" value="openshift-v2-prod"><br>' +
                        'Availability Zone: ' + '<input type="text" name="availability_zone" value="'+az+'"><br>' +
                        'Instance Type: ' + '<input type="text" name="instance_type" value="'+size+'"><br>' +
                        'Amount: ' + '<input type="text" name="amount" value="'+delta+'"><br>' +
                        '<button type="button" onclick="ajaxPurchase()">Purchase</button>' +
                      '</form>';
            $("#dialog").html(tbl)

            $("#dialog")
                .dialog({ title: size+' in '+az })
                .dialog("open");
        } );

    }); // end datatable.each()

    /* Formatting function for row details */
    function format_details (d) {
        // `d` is the original data object for the row
        var tbl = '<table class="details-table">'+
                    '<thead>'+
                    '<tr class="details-row">';
        if (d.expiration.length > 0) {
            tbl += '<td class="details-col">Account</td>'+
                    '<td class="details-col">RI Count</td>'+
                    '<td class="details-col">RI Days Left</td>'+
                    '<td class="details-col">RI End Date</td>'+
                    '</tr>'+
                    '</thead>'+
                    '<tbody>';
            for (el in d.expiration.sort(
                            function(a,b) {
                                return Number(a.days_left) - Number(b.days_left);
                            })
            ) {
                tbl += '<tr class="details-row">'+
                        '<td class="details-col">'+d.expiration[el].account+'</td>'+
                        '<td class="details-col">'+d.expiration[el].count+'</td>'+
                        '<td class="details-col">'+d.expiration[el].days_left+'</td>'+
                        '<td class="details-col">'+d.expiration[el].end_date+'</td>'+
                        '</tr>';
            }
        } else {
            tbl += '<td class="details-col">No reservation details to display</td>'+
                '</tr>'+
                '</thead>'+
                '<tbody>';
        }
        tbl += '</tbody>'+
                '</table>';
        return tbl;
    }
}) // end of document.ready()

/* tooltip */
$(function() {
    $( document ).tooltip();
});

function ajaxPurchase() {
    $.ajax({
        type : 'POST',
        url : 'purchase',
        dataType : 'json',
        encode : true,
        data : {
            'account' : $('input[name=account]').val(),
            'availability_zone' :  $('input[name=availability_zone]').val(),
            'instance_type' : $('input[name=instance_type]').val(),
            'amount' : $('input[name=amount]').val(),
        },
        success: function(data) {
            console.log(data);
            $("#dialog").dialog("close");
        },
        error: function(data) {
            console.log(data);
            $("#dialog").dialog().html('<pre>'+data['responseText']+'</pre>');
        },
    });
}

// ]]>
