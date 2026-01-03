"""Phase 4B Component Demo.

Shows usage of Phase 4B components:
- FileInput with Preview
- Tooltips & Popovers
- Figures
- EmptyState
- StatCard
- ConfirmDialog
- Hero
"""

from fasthtml.common import H2, H4, Div, FastHTML, P, serve

from faststrap import (
    Button,
    Card,
    Col,
    ConfirmDialog,
    Container,
    EmptyState,
    Figure,
    # New Components
    FileInput,
    Hero,
    Icon,
    Popover,
    Row,
    StatCard,
    Tooltip,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app)


@app.route("/")
def home():
    return Div(
        # 1. Hero
        Hero(
            "Phase 4B Showcase",
            "Enhanced Feedback, Forms, and Display Components",
            cta=Button("Get Started", variant="primary", size="lg"),
            bg_variant="dark",
            align="center",
            py="5",
            cls="mb-5",
        ),
        Container(
            # 2. Stats
            H2("Dashboard Stats (StatCard)", cls="mb-3"),
            Row(
                Col(
                    StatCard(
                        "Total Revenue",
                        "$124k",
                        trend="+12%",
                        trend_type="up",
                        icon=Icon("currency-dollar"),
                        icon_bg="bg-success-subtle",
                    ),
                    md=4,
                ),
                Col(
                    StatCard(
                        "Active Users",
                        "1,240",
                        trend="+5%",
                        trend_type="up",
                        icon=Icon("people"),
                        icon_bg="bg-primary-subtle",
                    ),
                    md=4,
                ),
                Col(
                    StatCard(
                        "Bounce Rate",
                        "42%",
                        trend="-2%",
                        trend_type="down",
                        icon=Icon("graph-down"),
                        icon_bg="bg-danger-subtle",
                    ),
                    md=4,
                ),
                cls="g-3 mb-5",
            ),
            # 3. Enhanced Inputs & Feedback
            Row(
                Col(
                    Card(
                        H4("File Input with Preview", cls="card-title"),
                        P(
                            "Upload an image to see the preview generated automatically via inline JS."
                        ),
                        FileInput(
                            "avatar",
                            label="Upload Avatar",
                            accept="image/*",
                            preview_id="auto",
                            helper_text="Supports PNG, JPG",
                        ),
                        body_cls="p-4",
                    ),
                    md=6,
                ),
                Col(
                    Card(
                        H4("Tooltips & Popovers", cls="card-title"),
                        P("Hover or click the buttons below."),
                        Div(
                            Tooltip("This is a tooltip!", Button("Hover Me", variant="secondary")),
                            Popover(
                                "Popover Title",
                                "This is the content.",
                                Button("Click Me", variant="info"),
                                placement="right",
                            ),
                            cls="d-flex gap-2",
                        ),
                        body_cls="p-4",
                    ),
                    md=6,
                ),
                cls="g-4 mb-5",
            ),
            # 4. Empty State
            H2("Empty State Pattern", cls="mb-3"),
            Card(
                EmptyState(
                    Icon("inbox", cls="display-1 text-muted mb-3"),
                    title="No New Messages",
                    description="You're all caught up! Check back later.",
                    action=Button("Refresh Inbox", variant="outline-primary"),
                ),
                cls="mb-5",
            ),
            # 5. Figure
            H2("Figures", cls="mb-3"),
            Row(
                Col(
                    Card(
                        Figure(
                            "https://placehold.co/600x400",
                            caption="A standard figure with caption",
                            fluid=True,
                            rounded=True,
                        ),
                        body_cls="p-3",
                    ),
                    md=6,
                ),
                Col(
                    Card(
                        Figure(
                            "https://placehold.co/150x150",
                            caption="Thumbnail",
                            thumbnail=True,
                            size="150px",
                        ),
                        body_cls="p-3 text-center",
                    ),
                    md=6,
                ),
                cls="g-4 mb-5",
            ),
            # 6. Confirm Dialog
            H2("Confirm Dialog", cls="mb-3"),
            Card(
                H4("Destructive Action", cls="card-title"),
                P("Clicking the button triggers a confirmation modal."),
                Button(
                    "Delete Account",
                    variant="danger",
                    data_bs_toggle="modal",
                    data_bs_target="#confirm-delete",
                ),
                ConfirmDialog(
                    "Are you absolutely sure you want to delete your account? This action cannot be undone.",
                    title="Delete Account?",
                    confirm_text="Yes, Delete",
                    cancel_text="Cancel",
                    variant="danger",
                    dialog_id="confirm-delete",
                    hx_confirm_url="#",  # Does nothing in demo
                ),
                body_cls="p-4",
            ),
            cls="mb-5",
        ),
    )


if __name__ == "__main__":
    serve(port=5003)
