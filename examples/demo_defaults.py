"""Example: Faststrap Defaults & Theming System

This example demonstrates the NEW resolve_defaults system:
1. How to set global component defaults (e.g., make ALL buttons secondary by default)
2. How explicit arguments override global defaults
3. How slot-classes work for Cards
"""

from fasthtml.common import H1, H2, Div, FastHTML, P, serve

from faststrap import (
    Button,
    Card,
    Col,
    Container,
    Row,
    add_bootstrap,
    set_component_defaults,
)

# Create the app
app = FastHTML()
add_bootstrap(app)


# ============================================================================
# EXAMPLE 1: Setting global defaults for Button
# ============================================================================
# After this call, ALL Button() calls without an explicit `variant` will be "secondary"
set_component_defaults("Button", variant="secondary")

# Similarly, we can set a default size
set_component_defaults("Button", size="lg")


# ============================================================================
# EXAMPLE 2: Setting global defaults for Card
# ============================================================================
# Let's style ALL card headers with a dark background by default
set_component_defaults("Card", header_cls="bg-dark text-white py-3")
set_component_defaults("Card", body_cls="p-4")


# ============================================================================
# Routes
# ============================================================================
@app.route("/")
def home():
    return Container(
        H1("Faststrap Defaults System Demo", cls="my-4"),
        # Section 1: Buttons
        Div(
            H2("1. Button Defaults", cls="mb-3"),
            P("After calling set_component_defaults('Button', variant='secondary', size='lg'),"),
            P("all buttons will be 'secondary' and 'lg' by default."),
            Row(
                Col(Button("Default Button"), cls="mb-2"),  # Will be secondary + lg
                Col(Button("Explicit Primary", variant="primary"), cls="mb-2"),  # Explicit wins
                Col(Button("Explicit Small", size="sm"), cls="mb-2"),  # Explicit size wins
                cls="g-3",
            ),
            cls="mb-5",
        ),
        # Section 2: Cards
        Div(
            H2("2. Card Slot-Class Defaults", cls="mb-3"),
            P(
                "After calling set_component_defaults('Card', header_cls='bg-dark text-white py-3'),"
            ),
            P("all cards with headers will have that style by default."),
            Row(
                Col(
                    Card(
                        "This card uses the global default header style.",
                        header="Default Header Styling",
                        title="Card 1",
                    ),
                    md=6,
                ),
                Col(
                    Card(
                        "This card overrides the header style with an explicit argument.",
                        header="Custom Header",
                        title="Card 2",
                        header_cls="bg-primary text-white py-2",  # Explicit wins
                    ),
                    md=6,
                ),
                cls="g-4",
            ),
            cls="mb-5",
        ),
        # Section 3: Combining Defaults
        Div(
            H2("3. Combining Everything", cls="mb-3"),
            P("This section shows a card with a button inside, both using defaults."),
            Card(
                P("This is the card body content."),
                Button("Save Changes"),  # Uses global secondary + lg
                Button("Cancel", variant="danger", size="sm", cls="ms-2"),  # Explicit overrides
                header="Action Card",
                title="Perform an Action",
            ),
            cls="mb-5",
        ),
        cls="py-4",
    )


# ============================================================================
# Run the app
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Run this example with: python examples/demo_defaults.py")
    print("Then visit: http://localhost:5001")
    print("=" * 60)
    serve(port=5001)
