from langchain_core.tools import tool


@tool
def create_account(account_code: str, account_name: str, account_type: str) -> str:
    """Create a new GL account in the Finance module.

    Args:
        account_code: Unique code for the account (e.g., '1001')
        account_name: Descriptive name of the account
        account_type: Type of account (e.g., Asset, Liability, Revenue, Expense)
    """
    return (
        f"Account created successfully.\n"
        f"  Code: {account_code}\n"
        f"  Name: {account_name}\n"
        f"  Type: {account_type}"
    )


@tool
def create_cost_center(cost_center_code: str, cost_center_name: str, description: str = "") -> str:
    """Create a new cost center in the Finance module.

    Args:
        cost_center_code: Unique code for the cost center (e.g., 'CC001')
        cost_center_name: Name of the cost center
        description: Optional description
    """
    return (
        f"Cost Center created successfully.\n"
        f"  Code: {cost_center_code}\n"
        f"  Name: {cost_center_name}\n"
        f"  Description: {description or 'N/A'}"
    )


@tool
def create_finance_year(year_code: str, start_date: str, end_date: str) -> str:
    """Create a new financial year in the Finance module.

    Args:
        year_code: Identifier for the finance year (e.g., 'FY2025')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
    """
    return (
        f"Finance Year created successfully.\n"
        f"  Year Code: {year_code}\n"
        f"  Period: {start_date} to {end_date}"
    )


@tool
def update_account(account_code: str, account_name: str = None, account_type: str = None) -> str:
    """Update an existing GL account.

    Args:
        account_code: Code of the account to update
        account_name: New name (optional)
        account_type: New type (optional)
    """
    updates = []
    if account_name:
        updates.append(f"Name → {account_name}")
    if account_type:
        updates.append(f"Type → {account_type}")
    return (
        f"Account '{account_code}' updated successfully.\n"
        f"  Changes: {', '.join(updates) if updates else 'No changes provided'}"
    )


FINANCE_TOOLS = [create_account, create_cost_center, create_finance_year, update_account]
