from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Float,
    Index,
    Integer,
    Text,
    String
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class AwsDetailedLineItem(Base):
    __tablename__ = 'aws_detailed_line_item'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, nullable=True)
    payer_account_id = Column(BigInteger, nullable=False)
    linked_account_id = Column(BigInteger, nullable=True)
    record_type = Column(String(64), nullable=False)
    record_id = Column(BigInteger, nullable=True)
    product_name = Column(String(255), nullable=True)
    rate_id = Column(Integer, nullable=True)
    subscription_id = Column(Integer, nullable=True)
    pricing_plan_id = Column(Integer, nullable=True)
    usage_type = Column(String(255), nullable=True)
    operation = Column(String(255), nullable=True)
    availability_zone = Column(String(64), nullable=True)
    reserved_instance = Column(Boolean, nullable=False)
    item_description = Column(String(255), nullable=True)
    usage_start_date = Column(DateTime, nullable=False)
    usage_end_date = Column(DateTime, nullable=False)
    usage_quantity = Column(Float, nullable=True)
    blended_rate = Column(Float, nullable=True)
    blended_cost = Column(Float, nullable=True)
    unblended_rate = Column(Float, nullable=True)
    unblended_cost = Column(Float, nullable=True)
    resource_id = Column(String(64), nullable=True)
    user_environment = Column(String(255), nullable=True)
    user_node = Column(String(255), nullable=True)

class AwsInvoiceLineItem(Base):
    __tablename__ = 'aws_invoice_line_item'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, nullable=True)
    payer_account_id = Column(BigInteger, nullable=False)
    linked_account_id = Column(BigInteger, nullable=True)
    record_type = Column(String(64), nullable=False)
    record_id = Column(BigInteger, nullable=True)
    product_name = Column(String(255), nullable=True)
    rate_id = Column(Integer, nullable=True)
    subscription_id = Column(Integer, nullable=True)
    pricing_plan_id = Column(Integer, nullable=True)
    usage_type = Column(String(255), nullable=True)
    operation = Column(String(255), nullable=True)
    availability_zone = Column(String(64), nullable=True)
    reserved_instance = Column(Boolean, nullable=False)
    item_description = Column(String(255), nullable=True)
    usage_start_date = Column(DateTime, nullable=False)
    usage_end_date = Column(DateTime, nullable=False)
    usage_quantity = Column(Float, nullable=True)
    blended_rate = Column(Float, nullable=True)
    blended_cost = Column(Float, nullable=True)
    unblended_rate = Column(Float, nullable=True)
    unblended_cost = Column(Float, nullable=True)
    resource_id = Column(String(64), nullable=True)
    user_environment = Column(String(255), nullable=True)
    user_node = Column(String(255), nullable=True)

class AwsCostAllocation(Base):
    __tablename__ = 'aws_cost_allocation'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(String(255), nullable=True)
    payer_account_id = Column(BigInteger, nullable=False)
    linked_account_id = Column(BigInteger, nullable=True)
    record_type = Column(String(64), nullable=False)
    record_id = Column(BigInteger, nullable=True)
    billing_period_start_date = Column(DateTime, nullable=False)
    billing_period_end_date = Column(DateTime, nullable=False)
    invoice_date = Column(DateTime, nullable=False)
    payer_account_name = Column(String(255), nullable=False)
    linked_account_name = Column(String(255), nullable=False)
    taxation_address = Column(String(255), nullable=False)
    payer_po_number = Column(Integer, nullable=False)
    product_code = Column(String(64), nullable=False)
    product_name = Column(String(255), nullable=True)
    seller_of_record = Column(String(255), nullable=False)
    usage_type = Column(String(255), nullable=True)
    operation = Column(String(255), nullable=True)
    availability_zone = Column(String(255), nullable=True)
    rate_id = Column(Integer, nullable=True)
    item_description = Column(String(255), nullable=True)
    usage_start_date = Column(DateTime, nullable=False)
    usage_end_date = Column(DateTime, nullable=False)
    usage_quantity = Column(Float, nullable=True)
    blended_rate = Column(Float, nullable=True)
    currency_code = Column(String(8), nullable=False)
    cost_before_tax = Column(Float, nullable=True)
    credits = Column(Float, nullable=True)
    tax_amount = Column(Float, nullable=True)
    tax_type = Column(String(255), nullable=False)
    total_cost = Column(Float, nullable=True)
    user_environment = Column(String(255), nullable=True)
    user_node = Column(String(255), nullable=True)

class AwsProduct(Base):
    __tablename__ = 'aws_product'

    id = Column(Integer, primary_key=True)
    sku = Column(String(64), nullable=False, unique=True)
    location = Column(String(64), nullable=False)
    instance_type = Column(String(64), nullable=False)
    current_generation = Column(Boolean, nullable=False)
    tenancy = Column(String(64), nullable=False)
    usage_type = Column(String(64), nullable=False)
    operation = Column(String(64), nullable=False)
    operating_system = Column(String(64), nullable=False)
    json = Column(Text(), nullable=True)

class AwsPrice(Base):
    __tablename__ = 'aws_price'

    id = Column(Integer, primary_key=True)
    sku = Column(String(64), nullable=False)
    offer_term_code = Column(String(64), nullable=False)
    price_dimensions = Column(Text(), nullable=True)
    term_attributes = Column(Text(), nullable=True)
    json = Column(Text(), nullable=True)

#XXX: half-baked idea - aggregate costs by product
#class AwsProductCostAggregate(Base):
#    __tablename__ = 'aws_product_cost_aggregate'
#    id = Column(Integer, primary_key=True)
#    linked_account_id = Column(BigInteger, nullable=True)
#    product_name = Column(String(255), nullable=True)
#    usage_start_date = Column(DateTime, nullable=False)
#    usage_end_date = Column(DateTime, nullable=False)
#    blended_cost = Column(Float, nullable=True)
#    unblended_cost = Column(Float, nullable=True)

class OpenshiftProfileStats(Base):
    __tablename__ = 'openshift_profile_stats'

    id = Column(Integer, primary_key=True)
    collection_date = Column(DateTime, nullable=False, unique=True)
    profile_name = Column(String(255), nullable=False)
    nodes_count = Column(Integer, nullable=True)
    gears_active_count = Column(Integer, nullable=True)
    gears_idle_count = Column(Integer, nullable=True)
    gears_stopped_count = Column(Integer, nullable=True)
    gears_unknown_count = Column(Integer, nullable=True)
    gears_total_count = Column(Integer, nullable=True)

class OpenshiftV3ProfileStats(Base):
    __tablename__ = 'openshift_v3_profile_stats'

    id = Column(Integer, primary_key=True)
    collection_date = Column(DateTime, nullable=False, unique=True)
    cluster_name = Column(String(64), nullable=False)
    compute_nodes = Column(Integer, nullable=False)
    compute_node_pod_capacity = Column(Integer, nullable=False)
    master_nodes = Column(Integer, nullable=False)
    master_node_pod_capacity = Column(Integer, nullable=False)
    unknown_nodes = Column(Integer, nullable=False)
    unknown_node_pod_capacity = Column(Integer, nullable=False)
    infra_nodes = Column(Integer, nullable=False)
    infra_node_pod_capacity = Column(Integer, nullable=False)
    total_pods = Column(Integer, nullable=False)
    total_containers = Column(Integer, nullable=False)
    active_containers = Column(Integer, nullable=False)
    terminated_containers = Column(Integer, nullable=False)
    terminating_containers = Column(Integer, nullable=False)
    waiting_containers = Column(Integer, nullable=False)
    running_containers = Column(Integer, nullable=False)
    failed_pods = Column(Integer, nullable=False)
    running_pods = Column(Integer, nullable=False)
    pending_pods = Column(Integer, nullable=False)
    succeeded_pods = Column(Integer, nullable=False)
    users = Column(Integer, nullable=False)
    projects = Column(Integer, nullable=False)
    active_projects = Column(Integer, nullable=False)
    terminating_projects = Column(Integer, nullable=False)

class AwsAccountMetadata(Base):
    __tablename__ = 'aws_account_metadata'

    id = Column(Integer, primary_key=True)
    account_id = Column(String(255), nullable=True, unique=True)
    account_name = Column(String(255), nullable=True)
    tags = Column(Text(), nullable=True)

class ExpensedCost(Base):
    __tablename__ = 'expensed_cost'

    id = Column(Integer, primary_key=True)
    vendor = Column(String(255), nullable=False)
    invoice_date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)

class GcpLineItem(Base):
    __tablename__ = 'gcp_line_item'

    id = Column(Integer, primary_key=True)
    project_name = Column(String(255), nullable=True)
    line_description = Column(String(255), nullable=False)
    line_id = Column(String(255), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    measured_amount = Column(Float, nullable=False)
    measured_unit = Column(String(255), nullable=False)
    cost_amount = Column(Float, nullable=False)
    cost_currency = Column(String(255), nullable=False)

class AwsInstanceInventory(Base):
    __tablename__ = 'aws_instance_inventory'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    environment = Column(String(64), nullable=True)
    instance_id = Column(String(64), nullable=False, unique=True)
    instance_type = Column(String(64), nullable=False)
    availability_zone = Column(String(64), nullable=False)
    account = Column(BigInteger, nullable=False)
    status = Column(String(16), nullable=False)
    launch_date = Column(DateTime, nullable=False)
    check_date = Column(DateTime, nullable=False)

class AwsReservationInventory(Base):
    __tablename__ = 'aws_reservation_inventory'

    id = Column(Integer, primary_key=True)
    reservation_id = Column(String(64), nullable=False, unique=True)
    instance_type = Column(String(64), nullable=False)
    availability_zone = Column(String(64), nullable=False)
    account = Column(BigInteger, nullable=False)
    purchase_date = Column(DateTime, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    instance_count = Column(Integer, nullable=False)


#class MyModel(Base):
#    __tablename__ = 'models'
#    id = Column(Integer, primary_key=True)
#    name = Column(Text)
#    value = Column(Integer)
#
#Index('my_index', MyModel.name, unique=True, mysql_length=255)
