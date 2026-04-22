from langchain_core.tools import tool


@tool
def create_supplier(
    supplier_code: str,
    supplier_name: str,
    contact_person: str = "",
    currency: str = "USD",
    country: str = "",
) -> str:
    """Create a new supplier in the SCM module.

    Args:
        supplier_code: Unique code for the supplier (e.g., 'SUP001')
        supplier_name: Name of the supplier
        contact_person: Primary contact name (optional)
        currency: Billing currency, default USD
        country: Country of the supplier (optional)
    """
    return (
        f"Supplier created successfully.\n"
        f"  Code: {supplier_code}\n"
        f"  Name: {supplier_name}\n"
        f"  Contact: {contact_person or 'N/A'}\n"
        f"  Currency: {currency}\n"
        f"  Country: {country or 'N/A'}"
    )


@tool
def create_warehouse(
    warehouse_code: str,
    warehouse_name: str,
    location: str = "",
    capacity: str = "",
) -> str:
    """Create a new warehouse in the SCM module.

    Args:
        warehouse_code: Unique code for the warehouse (e.g., 'WH001')
        warehouse_name: Name of the warehouse
        location: Physical address or location (optional)
        capacity: Storage capacity description (optional)
    """
    return (
        f"Warehouse created successfully.\n"
        f"  Code: {warehouse_code}\n"
        f"  Name: {warehouse_name}\n"
        f"  Location: {location or 'N/A'}\n"
        f"  Capacity: {capacity or 'N/A'}"
    )


@tool
def update_supplier(
    supplier_code: str,
    supplier_name: str = None,
    contact_person: str = None,
    currency: str = None,
) -> str:
    """Update an existing supplier record.

    Args:
        supplier_code: Code of the supplier to update
        supplier_name: New name (optional)
        contact_person: New contact person (optional)
        currency: New currency (optional)
    """
    updates = []
    if supplier_name:
        updates.append(f"Name → {supplier_name}")
    if contact_person:
        updates.append(f"Contact → {contact_person}")
    if currency:
        updates.append(f"Currency → {currency}")
    return (
        f"Supplier '{supplier_code}' updated successfully.\n"
        f"  Changes: {', '.join(updates) if updates else 'No changes provided'}"
    )


SCM_TOOLS = [create_supplier, create_warehouse, update_supplier]
