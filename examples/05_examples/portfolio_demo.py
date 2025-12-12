from fasthtml.common import H1, H2, H3, A, Div, FastHTML, Form, Main, P, serve

# from fasthtml.shorthands import Main
from faststrap import (
    # Display & Icons
    Badge,
    Button,
    ButtonGroup,
    Card,
    Col,
    # Layout & Containers
    Container,
    Icon,
    Input,
    # Feedback & Modals
    Modal,
    # Navigation & Interaction
    Navbar,
    Row,
    # Core
    add_bootstrap,
)

# --- Configuration ---
APP_TITLE = "Jane Doe - Expert Software Engineer"

app = FastHTML(title=APP_TITLE)
add_bootstrap(app, theme="dark", use_cdn=True)

# Inject Custom CSS for the Modern, Color-Attractive Look (Teal Accent)
ACCENT_COLOR = "#00FFFF"

app.hdrs.append(
    Div(
        style=f"""
        body {{ background-color: #1a1a1a; }} 
        .section-padding {{ padding: 6rem 0; }}
        .text-accent {{ color: {ACCENT_COLOR} !important; }}
        .btn-primary {{ 
            background-color: {ACCENT_COLOR} !important; 
            border-color: {ACCENT_COLOR} !important;
            color: #1a1a1a !important;
        }}
        .card {{ background-color: #2a2a2a; border: 1px solid #444; }}
        """
    )
)

# --- Components ---


def project_card(
    title: str,
    description: str,
    tech_stack: list[str],
    modal_id: str,
) -> Col:
    """Creates a Card for a portfolio project."""
    badges = [Badge(t, variant="secondary", cls="me-1") for t in tech_stack]

    return Col(
        Card(
            H3(title, cls="h5 card-title text-accent"),
            P(description, cls="card-text text-white-50"),
            Div(*badges, cls="mb-3"),
            Button(
                "View Details",
                variant="primary",
                data_bs_toggle="modal",
                data_bs_target=f"#{modal_id}",
            ),
            cls="h-100 shadow-lg",
        ),
        span=12,
        md=6,
        lg=4,
        cls="mb-4",
    )


def testimonial_card(quote: str, author: str, title: str) -> Col:
    """Creates a Card for a testimonial."""
    return Col(
        Card(
            Div(
                Icon("quote", cls="display-4 text-accent opacity-50"),
                P(quote, cls="lead fst-italic text-white"),
                P(
                    f"- {author}",
                    Badge(title, variant="info", pill=True),
                    cls="small text-white-75",
                ),
                cls="p-3",
            ),
            cls="h-100 shadow",
        ),
        span=12,
        md=6,
        cls="mb-4",
    )


# --- Sections ---


def hero_section() -> Main:
    """Home section with a striking CTA."""
    return Main(
        Container(
            Div(
                Badge("Expert Software Engineer", variant="primary", cls="mb-3"),
                H1(
                    "Building Scalable Systems with ",
                    Div("Python & HTMX.", cls="d-block text-accent text-shadow"),
                    cls="display-1 fw-bolder text-white mb-4",
                ),
                P(
                    "5+ years of experience designing and deploying high-performance web applications and systems architecture.",
                    cls="lead text-white-75 mb-5",
                ),
                ButtonGroup(
                    Button(
                        Icon("arrow-down-right-circle", cls="me-2"),
                        "View Portfolio",
                        variant="primary",
                        href="#portfolio",
                    ),
                    Button(
                        Icon("file-text", cls="me-2"),
                        "Download Resume",
                        variant="outline-light",
                        cls="ms-2",
                    ),
                ),
                cls="text-center py-5",
                style="min-height: 80vh; display: flex; flex-direction: column; justify-content: center;",
            ),
        ),
        id="home",
    )


def about_section() -> Div:
    """About Me section with key skills."""
    skills = [
        ("Python/FastAPI", "success"),
        ("FastHTML/HTMX", "info"),
        ("Docker/Kubernetes", "primary"),
        ("PostgreSQL/Redis", "warning"),
        ("AWS/GCP", "danger"),
        ("System Design", "secondary"),
    ]

    return Div(
        Container(
            H2("About Me", cls="display-5 fw-bold text-white text-center mb-5"),
            Row(
                Col(
                    P(
                        "As a seasoned expert, my focus is on architectural efficiency and code correctness. I specialize in building robust, performant backend systems and coupling them with clean, interactive front-ends using the principles of HATEOAS and the power of HTMX.",
                        cls="lead text-white-75 mb-4",
                    ),
                    P(
                        "The core of my work revolves around microservices, cloud-native deployments, and ensuring every line of code meets production-level standards. I thrive in environments that prioritize scalability and developer experience.",
                        cls="text-white-50",
                    ),
                    Button("Contact Me", variant="accent", href="#contact", cls="mt-4"),
                    span=12,
                    lg=6,
                ),
                Col(
                    Div(
                        H3("Expertise", cls="h4 text-accent mb-3"),
                        *[Badge(s, variant=v, cls="me-2 mb-2 p-2 fs-6") for s, v in skills],
                    ),
                    span=12,
                    lg=6,
                ),
            ),
        ),
        id="about",
        cls="section-padding bg-darker",
    )


def portfolio_section() -> Div:
    """Portfolio section using Card components in a grid."""
    projects = [
        (
            "FastTracker",
            "A real-time data ingestion and visualization platform built with FastAPI and Redis.",
            ["Python", "FastAPI", "Redis", "HTMX"],
            "modal1",
        ),
        (
            "E-Commerce API",
            "Designed and deployed a highly scalable RESTful API with advanced caching and payment gateway integration.",
            ["Go", "Docker", "PostgreSQL", "Kafka"],
            "modal2",
        ),
        (
            "Component Library",
            "The open-source library that built this site. Focus on Bootstrap component encapsulation.",
            ["Python", "FastHTML", "Bootstrap 5"],
            "modal3",
        ),
    ]

    return Div(
        Container(
            H2("Portfolio", cls="display-5 fw-bold text-white text-center mb-5"),
            Row(*[project_card(*p) for p in projects]),
        ),
        id="portfolio",
        cls="section-padding",
    )


def testimonials_section() -> Div:
    """Testimonials section with Card components."""
    testimonials = [
        (
            "Jane's system architecture improved our deploy time by 40%. A true professional.",
            "Sarah K.",
            "CTO, GlobalTech",
        ),
        (
            "The component-based approach she championed has made our codebase infinitely more maintainable.",
            "Mark V.",
            "Lead Frontend Dev",
        ),
    ]

    return Div(
        Container(
            H2("Client Feedback", cls="display-5 fw-bold text-white text-center mb-5"),
            Row(*[testimonial_card(*t) for t in testimonials]),
        ),
        id="testimonials",
        cls="section-padding bg-darker",
    )


def contact_section() -> Div:
    """Contact section using Input and Button components."""
    return Div(
        Container(
            H2("Get In Touch", cls="display-5 fw-bold text-white text-center mb-5"),
            Row(
                Col(
                    Form(
                        Input("name", label="Full Name", placeholder="Your Name", required=True),
                        Input(
                            "email",
                            input_type="email",
                            label="Email Address",
                            placeholder="your@email.com",
                            required=True,
                        ),
                        Input(
                            "message",
                            input_type="textarea",
                            label="Your Message",
                            placeholder="I'd like to discuss...",
                            rows=5,
                        ),
                        Button(
                            Icon("send-fill", cls="me-2"),
                            "Send Message",
                            variant="primary",
                            type="submit",
                            cls="mt-4 w-100",
                        ),
                        cls="p-4 rounded shadow-lg card",
                    ),
                    span=12,
                    md=8,
                    lg=6,
                    cls="mx-auto",  # Center the form
                ),
            ),
        ),
        id="contact",
        cls="section-padding",
    )


def footer_content() -> Div:
    """Simple footer for professionalism."""
    return Div(
        Container(
            P(
                Icon("code-slash", cls="me-1"),
                "Built with ",
                A(
                    "FastStrap",
                    href="https://github.com/Evayoung/Faststrap",
                    target="_blank",
                    cls="text-accent",
                ),
                " and FastHTML. © 2025",
                cls="text-center text-white-50 small mb-0 py-3",
            )
        ),
        cls="border-top border-secondary mt-5",
    )


# --- Modals (Hidden Content) ---


def project_modals() -> Div:
    """Hidden modals for project details."""
    return Div(
        Modal(
            Div(
                P(
                    "The **FastTracker** project involved designing a non-blocking ingestion pipeline using Python's `asyncio` and leveraging Redis Streams for high-throughput messaging. It handles peak loads of 10,000 requests/second."
                ),
                P(
                    "The frontend utilizes HTMX for dynamic updates of charts and tables, minimizing JavaScript overhead."
                ),
            ),
            modal_id="modal1",
            title="FastTracker Project Details",
            size="lg",
        ),
        Modal(
            Div(P("Details for E-Commerce API...")),
            modal_id="modal2",
            title="E-Commerce API Details",
        ),
        Modal(
            Div(P("Details for Component Library...")),
            modal_id="modal3",
            title="Component Library Details",
        ),
    )


# --- Application Route ---


@app.route("/")
def portfolio_home():
    """Renders the entire multi-section portfolio page."""
    return Div(
        # Top Navigation
        Navbar(
            A("Home", href="#home", cls="nav-link active"),
            A("About", href="#about", cls="nav-link"),
            A("Work", href="#portfolio", cls="nav-link"),
            A("Contact", href="#contact", cls="nav-link"),
            brand="Jane Doe",
            brand_href="#home",
            variant="dark",
            bg="dark",
            expand="lg",
            fixed="top",  # Stick the navbar to the top
            cls="shadow-lg",
        ),
        # Spacer for fixed navbar (Best practice)
        Div(style="height: 56px;"),
        # Content Sections
        hero_section(),
        about_section(),
        portfolio_section(),
        testimonials_section(),
        contact_section(),
        # Footer
        footer_content(),
        # Hidden Components
        project_modals(),
    )


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(f"🚀 Running {APP_TITLE} Portfolio Demo")
    print("📍 Visit: http://localhost:5001")
    print("=" * 70)
    serve()
