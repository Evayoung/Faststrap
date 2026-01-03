"""Faststrap Layouts & Patterns Demo.

Showcasing Phase 5B: DashboardLayout, LandingLayout, and Modern UI Patterns.
"""

from fasthtml.common import H2, A, Div, FastHTML, Footer, P, serve

from faststrap import (
    Badge,
    Button,
    Card,
    DashboardLayout,
    Feature,
    FeatureGrid,
    Fx,
    Hero,
    Icon,
    LandingLayout,
    NavbarModern,
    PricingGroup,
    PricingTier,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", font_family="Outfit")


@app.route("/")
def home():
    # Modern Glass Navbar
    nav = NavbarModern(
        brand=Div(Icon("stars", cls="me-2 text-primary"), "Faststrap Pro"),
        items=[
            A("Features", href="#features", cls="nav-link"),
            A("Pricing", href="#pricing", cls="nav-link"),
            Button("Get Started", cls="btn-primary ms-lg-3"),
        ],
        glass=True,
    )

    # Hero Section
    hero = Hero(
        title="Build Professional Layouts in Minutes",
        subtitle="The zero-JS, pure Python framework for Bootstrap 5 and FastHTML.",
        cta=Div(
            Button("View Dashboard", href="/dashboard", cls="btn-primary btn-lg px-5 me-2"),
            Button("Documentation", href="#", cls="btn-outline-primary btn-lg px-5"),
            cls="d-flex justify-content-center mt-4",
        ),
        cls=f"{Fx.fade_in_up}",
    )

    # features
    features = FeatureGrid(
        Feature(
            "Zero JS",
            "Everything is powered by pure CSS and Python logic.",
            icon="lightning-charge",
            icon_cls="bg-warning-subtle text-warning",
        ),
        Feature(
            "Responsive",
            "Mobile-first layouts that look great on any device.",
            icon="phone",
            icon_cls="bg-info-subtle text-info",
        ),
        Feature(
            "Modern",
            "Glassmorphism, hover effects, and premium aesthetics.",
            icon="gem",
            icon_cls="bg-primary-subtle text-primary",
        ),
        cols=3,
        id="features",
        cls="py-5",
    )

    # Pricing
    pricing = Div(
        H2("Simple, Transparent Pricing", cls="text-center mb-5"),
        PricingGroup(
            PricingTier(
                "Starter",
                "$0",
                ["1 Project", "Basic Components", "Community Support"],
                cta=Button("Current Plan", cls="btn-outline-primary w-100", disabled=True),
            ),
            PricingTier(
                "Pro",
                "$29",
                ["Unlimited Projects", "Premium Layouts", "Priority Support", "Custom Themes"],
                featured=True,
                cta=Button("Go Pro", cls="btn-primary w-100"),
            ),
            PricingTier(
                "Enterprise",
                "$99",
                ["Custom Development", "Team Management", "SLA Guarantee", "On-premise"],
                cta=Button("Contact Sales", cls="btn-outline-primary w-100"),
            ),
        ),
        id="pricing",
        cls="py-5",
    )

    footer = Footer(
        Div(
            Div("© 2026 Faststrap. Built with FastHTML.", cls="text-muted"),
            cls="container text-center py-4 border-top mt-5",
        )
    )

    return LandingLayout(hero, features, pricing, navbar=nav, footer=footer)


@app.get("/dashboard")
def dashboard():
    # Sidebar items
    items = [
        A(Div(Icon("house", cls="me-2"), "Overview"), href="#", cls="nav-link active"),
        A(Div(Icon("bar-chart", cls="me-2"), "Analytics"), href="#", cls="nav-link text-reset"),
        A(Div(Icon("people", cls="me-2"), "Customers"), href="#", cls="nav-link text-reset"),
        A(Div(Icon("gear", cls="me-2"), "Settings"), href="#", cls="nav-link text-reset"),
    ]

    # Content
    stats = Div(
        Row(
            Col(
                Card(
                    Div(
                        P("Total Sales", cls="text-muted small"),
                        H2("$12,450"),
                        Badge("+15%", variant="success"),
                    ),
                    cls="border-0 shadow-sm",
                )
            ),
            Col(
                Card(
                    Div(
                        P("Active Users", cls="text-muted small"),
                        H2("1,280"),
                        Badge("+5%", variant="success"),
                    ),
                    cls="border-0 shadow-sm",
                )
            ),
            Col(
                Card(
                    Div(
                        P("Conversion", cls="text-muted small"),
                        H2("3.2%"),
                        Badge("-2%", variant="danger"),
                    ),
                    cls="border-0 shadow-sm",
                )
            ),
        ),
        cls="mb-4",
    )

    main_card = Card(
        "Welcome to your professional dashboard layout. This sidebar is responsive and will collapse on smaller screens.",
        header="Dashboard Overview",
        footer=Button("Refresh Data", cls="btn-sm btn-primary"),
        cls="border-0 shadow-sm",
    )

    user_dropdown = Div("User Profile", cls="badge bg-light text-dark p-2 rounded-pill shadow-sm")

    return DashboardLayout(
        stats,
        main_card,
        sidebar_items=items,
        user=user_dropdown,
        footer="Faststrap Admin Panel v1.0",
    )


if __name__ == "__main__":
    serve(port=5011)
