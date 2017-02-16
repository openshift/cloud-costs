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
                { 'data' : 'account', 'className' : 'account-number' },
                { 'data' : 'zone', 'className' : 'availability-zone' },
                { 'data' : 'type', 'className' : 'instance-type' },
                {
                    'data' : 'running',
                    'className' : 'running-count',
                    'render' : function (data, type, full, meta) {
                        return '<a href="#" class="runningCountLink">'+data+'</a>';
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
                    'defaultContent' : '<p class="purchaseButton">Purchase</p>'
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
        $('table.datatable#'+$(this).attr("id")+' tbody').on('click', 'a.runningCountLink', function () {
            var row = $(this).closest("tr");
            var account = $(this).closest("table.results_table").attr('id');
            var az = row.children("td.availability-zone").text();
            var size = row.children("td.instance-type").text();

            var tbl = '<table class="instancesTable"></table>';
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
            var tbl = '<form class="purchaseForm" method="post">' +
                        '<div class="purchaseForm">'+
                            'Account: ' + '<input class="purchaseForm" type="text" name="account" value="openshift-v2-prod">'+
                        '</div>' +
                        '<div class="purchaseForm">'+
                            'Platform: ' + '<input class="purchaseForm" type="text" name="platform" value="Linux/UNIX (Amazon VPC)">' +
                        '</div>' +
                        '<div class="purchaseForm">'+
                            'Region: ' + '<input class="purchaseForm" type="text" name="region" value="'+az.slice(0,az.length-1)+'">' +
                        '</div>' +
                        '<div class="purchaseForm">'+
                            'Availability Zone: ' + '<input class="purchaseForm" type="text" name="availability_zone">' +
                        '</div>' +
                        '<div class="purchaseForm">'+
                            'Instance Type: ' + '<input class="purchaseForm" type="text" name="instance_type" value="'+size+'"> ' +
                        '</div>' +
                        '<div class="purchaseForm">'+
                            'Offering Class: ' + '<select class="purchaseForm" name="offering_class">'+
                                '<option selected="1">convertible</option>' +
                                '<option>standard</option>' +
                            '</select>' +
                        '</div>' +
                        '<div class="purchaseForm">'+
                            'Payment Option: ' + '<select class="purchaseForm" name="payment_option">'+
                                '<option selected="1">Partial Upfront</option>' +
                                '<option>No Upfront</option>' +
                                '<option>All Upfront</option>' +
                                '<option>Light Utilization</option>' +
                                '<option>Medium Utilization</option>' +
                            '</select> ' +
                        '</div>' +
                        '<div class="purchaseForm">'+
                            'Duration: ' + '<select class="purchaseForm" name="max_duration">'+
                                '<option selected="1" value="31536000">0-12 months</option>' +
                                '<option value="94608000">13-36 months</option>' +
                            '</select><br>' +
                        '</div>' +
                        '<div class="purchaseForm">'+
                            'Amount: ' + '<input class="purchaseForm" type="text" name="amount" value="'+delta+'"><br>' +
                        '</div>' +
                        '<div class="purchaseForm">'+
                            '<button id="searchButton" name="searchButton" type="button" onclick="ajaxOfferingSearch()">Search</button>' +
                        '</div>' +
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
        var tbl = '<table class="detailsTable">'+
                    '<thead>'+
                    '<tr class="detailsRow">';
        if (d.expiration.length > 0) {
            tbl += '<td class="detailsCol">Account</td>'+
                    '<td class="detailsCol">RI Count</td>'+
                    '<td class="detailsCol">RI Days Left</td>'+
                    '<td class="detailsCol">RI End Date</td>'+
                    '</tr>'+
                    '</thead>'+
                    '<tbody>';
            for (el in d.expiration.sort(
                            function(a,b) {
                                return Number(a.days_left) - Number(b.days_left);
                            })
            ) {
                tbl += '<tr class="detailsRow">'+
                        '<td class="detailsCol">'+d.expiration[el].account+'</td>'+
                        '<td class="detailsCol">'+d.expiration[el].count+'</td>'+
                        '<td class="detailsCol">'+d.expiration[el].days_left+'</td>'+
                        '<td class="detailsCol">'+d.expiration[el].end_date+'</td>'+
                        '</tr>';
            }
        } else {
            tbl += '<td class="detailsCol">No reservation details to display</td>'+
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

function ajaxOfferingSearch() {
    $("div#offeringSearchResults").remove();

    $.ajax({
        type : 'POST',
        url : 'search_offerings',
        dataType : 'json',
        encode : true,
        data : {
            'account' : $('input[name=account]').val(),
            'platform' :  $('input[name=platform]').val(),
            'region' :  $('input[name=region]').val(),
            'availability_zone' :  $('input[name=availability_zone]').val(),
            'instance_type' : $('input[name=instance_type]').val(),
            'offering_class' : $('select[name=offering_class]').val(),
            'payment_option' : $('select[name=payment_option]').val(),
            'amount' : $('input[name=amount]').val(),
            'max_duration' : $('select[name=max_duration]').val(),
            'min_duration' : $('select[name=max_duration]').val() == 94608000 ? 31536001 : 0 ,
        },
        success: function(data) {
            var searchResults = '<form class="confirmForm" method="post">' +
                                '<div id="offeringSearchResults">'+
                                '<p>'+data['offerings'].length+' Offerings Found.</p>';

            var offerings = data['offerings'];
            if (offerings.length > 0) {
                searchResults += '<div class="offeringSearch">'+
                                    '<span class="offeringSearchRadio"></span>'+
                                    '<span class="offeringSearch">Availability Zone</span>'+
                                    '<span class="offeringSearch">Scope</span>'+
                                    '<span class="offeringSearch">Duration</span>'+
                                    '<span class="offeringSearch">Up Front</span>'+
                                    '<span class="offeringSearch">Metered Rate</span>'+
                                    '</div>';
                for (i=0; i<offerings.length; i++) {
                    searchResults += '<div class="offeringSearch">'+
                                        '<span class="offeringSearchRadio">'+
                                            '<input type="radio" name="reservation_id" value="'+offerings[i]['ReservedInstancesOfferingId']+'">'+
                                        '</span>'+
                                        '<span class="offeringSearch">'+offerings[i]['AvailabilityZone']+'</span>'+
                                        '<span class="offeringSearch">'+offerings[i]['Scope']+'</span>'+
                                        '<span class="offeringSearch">'+(offerings[i]['Duration']/24/60/60)+' days</span>';
                    if (offerings[i]['CurrencyCode'] == 'USD') {
                        searchResults += '<span class="offeringSearch">$ '+offerings[i]['FixedPrice']+'</span>';
                    } else {
                        searchResults += '<span class="offeringSearch">'+offerings[i]['FixedPrice']+
                                                                    ' '+offerings[i]['CurrencyCode']+'</span>';
                    }
                    if (offerings[i]['RecurringCharges'].length > 0) {
                        if (offerings[i]['CurrencyCode'] == 'USD') {
                            searchResults += '<span class="offeringSearch">$ '+offerings[i]['RecurringCharges'][0]['Amount']+
                                        ' '+offerings[i]['RecurringCharges'][0]['Frequency']+'</span>';
                        } else {
                            searchResults += '<span class="offeringSearch">'+offerings[i]['RecurringCharges'][0]['Amount']+
                                        ' '+offerings[i]['CurrencyCode']+
                                        ' '+offerings[i]['RecurringCharges'][0]['Frequency']+'</span>';
                        }
                    } else {
                        searchResults += '<span class="offeringSearch">$0.00</span>';
                    };
                    searchResults += '</div>';
                };
            };
            searchResults += '<div class="offeringSearch">'+
                                '<button id="purchaseButton" name="purchaseButton" type="button" onclick="ajaxOfferingPurchase()" disabled=1>Purchase</button>' +
                             '</div>';
            searchResults += '</div></form>';

            $("#dialog").dialog().append(searchResults);

            if (data['offerings'].length > 0) {
                $('#purchaseButton').removeAttr('disabled');
                $('#searchButton').attr('disabled', '1');
            } else {
                $('#purchaseButton').attr('disabled', '1');
                $('#searchButton').removeAttr('disabled');
            };
        },
        error: function(data) {
            $("#dialog").dialog().html('<pre>'+data['responseText']+'</pre>');
        },
    });
}

function ajaxOfferingPurchase() {
    $.ajax({
        type : 'POST',
        url : 'purchase',
        dataType : 'json',
        encode : true,
        data : {
            'account' : $('input[name=account]').val(),
            'region' : $('input[name=region]').val(),
            'instance_count' : $('input[name=amount]').val(),
            'reservation_id' :  $('input[name=reservation_id]').val(),
        },
        success: function(data) {
            $("#dialog").dialog("close");
        },
        error: function(data) {
            //TODO: pretty up the error output
            $("#dialog").dialog().html('<pre>'+data['responseText']+'</pre>');
        },
    });
}

// ]]>
