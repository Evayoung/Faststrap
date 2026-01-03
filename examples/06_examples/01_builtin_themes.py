from fasthtml.common import *

from faststrap import *

# 1. Initialize the app
app = FastHTML()

# 2. Add Bootstrap ONCE at the app level
# The mode="auto" generates CSS that works for light, dark, and system preference.
add_bootstrap(app, theme="cosmo", mode="auto")


@app.route("/")
def home():
    return Titled(
        "Faststrap Built-in Themes",
        Container(
            Card(
                Section(
                    H2("Built-in Theme: Cosmo"),
                    P(
                        "This example demonstrates instantaneous toggling between light and dark modes."
                    ),
                    Div(
                        # Direct client-side attribute update for 'Wow' speed
                        Button(
                            "Switch to Light",
                            onclick="document.documentElement.setAttribute('data-bs-theme', 'light')",
                            variant="light",
                            cls="me-2",
                        ),
                        Button(
                            "Switch to Dark",
                            onclick="document.documentElement.setAttribute('data-bs-theme', 'dark')",
                            variant="dark",
                            cls="me-2",
                        ),
                        cls="mb-4",
                    ),
                    Hr(),
                    Grid(
                        Div(
                            H4("Buttons"),
                            Div(
                                Button("Primary", variant="primary", cls="me-1"),
                                Button("Secondary", variant="secondary", cls="me-1"),
                                Button("Success", variant="success", cls="me-1"),
                                Button("Danger", variant="danger", cls="me-1"),
                                cls="mb-3",
                            ),
                            H4("Badges"),
                            Div(
                                Badge("New", variant="primary", cls="me-1"),
                                Badge("Update", variant="success", pill=True, cls="me-1"),
                                Badge("Alert", variant="danger", cls="me-1"),
                            ),
                        ),
                        Div(
                            H4("Alerts"),
                            Alert("This is a success alert!", variant="success"),
                            Alert("Be careful with this one.", variant="warning"),
                        ),
                    ),
                    cls="p-4",
                )
            ),
            cls="mt-5",
        ),
    )


if __name__ == "__main__":
    serve()
