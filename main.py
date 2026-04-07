from datetime import datetime
from typing import Dict, List
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("LeaveManager", json_response=True)

# In-memory leave store
leave_requests: List[Dict] = []
employees = {
    "E001": {"name": "Alice Johnson", "department": "Engineering", "leave_balance": 15},
    "E002": {"name": "Bob Smith", "department": "HR", "leave_balance": 12},
    "E003": {"name": "Charlie Brown", "department": "Finance", "leave_balance": 10},
}


# Tool: Apply for leave
@mcp.tool()
def apply_leave(employee_id: str, start_date: str, end_date: str, reason: str) -> Dict:
    """Apply for leave for an employee"""
    if employee_id not in employees:
        return {"status": "error", "message": "Employee not found"}

    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return {"status": "error", "message": "Dates must be in YYYY-MM-DD format"}

    if end < start:
        return {"status": "error", "message": "End date cannot be before start date"}

    days_requested = (end - start).days + 1
    employee = employees[employee_id]

    if employee["leave_balance"] < days_requested:
        return {
            "status": "error",
            "message": f"Insufficient leave balance. Available: {employee['leave_balance']} days"
        }

    request_id = f"L{len(leave_requests) + 1:03d}"
    leave_request = {
        "request_id": request_id,
        "employee_id": employee_id,
        "employee_name": employee["name"],
        "start_date": start_date,
        "end_date": end_date,
        "days": days_requested,
        "reason": reason,
        "status": "Pending"
    }

    leave_requests.append(leave_request)

    return {
        "status": "success",
        "message": "Leave request submitted successfully",
        "request": leave_request
    }


# Tool: Approve leave
@mcp.tool()
def approve_leave(request_id: str) -> Dict:
    """Approve a leave request"""
    for request in leave_requests:
        if request["request_id"] == request_id:
            if request["status"] != "Pending":
                return {"status": "error", "message": f"Request is already {request['status']}"}

            employee = employees[request["employee_id"]]
            employee["leave_balance"] -= request["days"]
            request["status"] = "Approved"

            return {
                "status": "success",
                "message": f"Leave request {request_id} approved",
                "remaining_balance": employee["leave_balance"]
            }

    return {"status": "error", "message": "Request not found"}


# Tool: Reject leave
@mcp.tool()
def reject_leave(request_id: str) -> Dict:
    """Reject a leave request"""
    for request in leave_requests:
        if request["request_id"] == request_id:
            if request["status"] != "Pending":
                return {"status": "error", "message": f"Request is already {request['status']}"}

            request["status"] = "Rejected"
            return {
                "status": "success",
                "message": f"Leave request {request_id} rejected"
            }

    return {"status": "error", "message": "Request not found"}


# Tool: Check leave balance
@mcp.tool()
def check_leave_balance(employee_id: str) -> Dict:
    """Check leave balance for an employee"""
    if employee_id not in employees:
        return {"status": "error", "message": "Employee not found"}

    employee = employees[employee_id]
    return {
        "employee_id": employee_id,
        "employee_name": employee["name"],
        "department": employee["department"],
        "leave_balance": employee["leave_balance"]
    }


# Tool: View all leave requests
@mcp.tool()
def get_all_leave_requests() -> List[Dict]:
    """Get all leave requests"""
    return leave_requests


# Resource: Employee details
@mcp.resource("employee://{employee_id}")
def get_employee(employee_id: str) -> Dict:
    """Get employee details"""
    if employee_id not in employees:
        return {"status": "error", "message": "Employee not found"}

    return employees[employee_id]


# Prompt: Generate leave request email
@mcp.prompt()
def leave_request_email(employee_name: str, start_date: str, end_date: str, reason: str) -> str:
    """Generate a professional leave request email"""
    return (
        f"Write a professional leave request email for employee {employee_name}, "
        f"requesting leave from {start_date} to {end_date} due to {reason}."
    )


if __name__ == "__main__":
    mcp.run(transport="streamable-http")