app_name = "buzz_custom"
app_title = "Buzz Custom"
app_publisher = "Corono"
app_description = "Customizations for Buzz"
app_email = "ashwinkumark59@gmail.com"
app_license = "mit"

required_apps = ["buzz"]

fixtures = [

    # 🧩 Customization
    {
        "dt": "Custom Field",
        "filters": [["module", "=", "buzz_custom"]]
    },
    {
        "dt": "Property Setter",
        "filters": [["module", "=", "buzz_custom"]]
    },
    {
        "dt": "Custom DocPerm",
        "filters": [["module", "=", "buzz_custom"]]
    },

    # ⚙️ Scripts
    {
        "dt": "Client Script",
        "filters": [["module", "=", "buzz_custom"]]
    },
    {
        "dt": "Server Script",
        "filters": [["module", "=", "buzz_custom"]]
    },

    # 🔁 Workflow
    {
        "dt": "Workflow",
        "filters": [["is_active", "=", 1]]
    },
    {
        "dt": "Workflow State",
        "filters": [["name", "in", []]]
    },
    {
        "dt": "Workflow Action Master",
        "filters": [["name", "in", []]]
    },

    # 📧 Notifications
    {
        "dt": "Notification",
        "filters": [["name", "in", []]]
    },

    # 📧 Email Templates
    {
        "dt": "Email Template",
        "filters": [["name", "in", []]]
    },

    # 🌐 Website
    {
        "dt": "Web Page",
        "filters": [["module", "=", "buzz_custom"]]
    },
    {
        "dt": "Web Form",
        "filters": [["module", "=", "buzz_custom"]]
    },

    # 🖨️ Print & Reports
    {
        "dt": "Print Format",
        "filters": [["module", "=", "buzz_custom"]]
    },
    {
        "dt": "Report",
        "filters": [["module", "=", "buzz_custom"]]
    },

    # 🖥️ Workspace
    {
        "dt": "Workspace",
        "filters": [["module", "=", "buzz_custom"]]
    },

    # 🔐 Roles
    {
        "dt": "Role",
        "filters": [["name", "in", []]]
    },
]
