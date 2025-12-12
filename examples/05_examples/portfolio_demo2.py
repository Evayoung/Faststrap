from fasthtml.common import (
    H1,
    H2,
    H4,
    A,
    Col,
    Div,
    FastHTML,
    Form,
    Img,
    Label,
    Li,
    P,
    Textarea,
    Ul,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Button,
    Card,
    Container,
    Icon,
    Input,
    Navbar,
    Row,
    TabPane,
    Tabs,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="dark", use_cdn=True)


# ============================================================
# NAVBAR
# ============================================================
navbar = Navbar(
    Div(
        A("Home", href="#home", cls="nav-link active"),
        A("About", href="#about", cls="nav-link"),
        A("Portfolio", href="#portfolio", cls="nav-link"),
        A("Testimonials", href="#testimonials", cls="nav-link"),
        A("Contact", href="#contact", cls="nav-link"),
        cls="navbar-nav me-auto",
    ),
    Div(Button("Download CV", variant="outline-light", size="sm"), cls="d-flex"),
    brand="👨‍💻 Meshell Dev",
    brand_href="#home",
    variant="dark",
    bg="primary",
    expand="lg",
    cls="shadow-sm",
)


# ============================================================
# HERO SECTION
# ============================================================
def hero_section():
    return Container(
        Div(
            H1(
                Icon("lightning-charge-fill", cls="text-warning me-2"),
                "Crafting Reliable Engineering & AI Solutions",
                cls="display-4 fw-bold mb-3",
            ),
            P(
                "I am a software engineer specializing in Python, FastAPI, Kivy, "
                "distributed systems, machine learning, and elegant solution architecture.",
                cls="lead text-white-50 mb-4",
            ),
            Button("See My Work", href="#portfolio", variant="warning", size="lg", cls="px-4 py-2"),
            cls="text-center py-5 rounded-4",
            style="background: linear-gradient(135deg,#5337ff 0%,#8f3cff 100%);",
        ),
        cls="my-5",
    )


# ============================================================
# ABOUT SECTION
# ============================================================
def about_section():
    return Container(
        Div(
            H2("About Me", cls="fw-bold mb-3"),
            P(
                "I’m Meshell, a highly skilled software engineer with expertise in API design, "
                "AI agents, distributed systems, cross-platform apps, and innovative software architecture.",
                cls="lead mb-4",
            ),
            Row(
                Col(
                    Card(
                        H4("Skills", cls="mb-3"),
                        Ul(
                            Li("Python / FastAPI / Reflex"),
                            Li("Distributed Systems & Containers"),
                            Li("Machine Learning & AI Agents"),
                            Li("Kivy / KivyMD / PySide / Flet"),
                            Li("SQLAlchemy / PostgreSQL / Redis"),
                            cls="mb-0",
                        ),
                        header=Badge("Tech Stack", variant="primary"),
                        cls="shadow-sm",
                    ),
                    span=12,
                    md=6,
                ),
                Col(
                    Card(
                        H4("Experience", cls="mb-3"),
                        P(
                            "5+ years building robust systems across multiple industries:",
                            cls="mb-2",
                        ),
                        Ul(
                            Li("Financial systems & cooperative platforms"),
                            Li("QR-code verification systems (QRive)"),
                            Li("Mobile apps for offline-first workflows"),
                            Li("SaaS dashboards & automation tools"),
                        ),
                        header=Badge("Experience", variant="success"),
                        cls="shadow-sm",
                    ),
                    span=12,
                    md=6,
                ),
                cls="g-4",
            ),
            cls="py-5",
            id="about",
        )
    )


# ============================================================
# PORTFOLIO SECTION
# ============================================================
def portfolio_section():
    return Container(
        Div(
            H2("Portfolio", cls="fw-bold mb-4"),
            P("Some featured work:", cls="text-white-50 mb-4"),
            Row(
                *[
                    Col(
                        Card(
                            Img(
                                src=f"https://picsum.photos/seed/{i}/600/400",
                                cls="card-img-top rounded",
                            ),
                            Div(
                                H4(f"Project {i+1}", cls="fw-bold"),
                                P("A description of what the project achieves."),
                                Button("View Details", variant="primary", size="sm"),
                                cls="mt-2",
                            ),
                            cls="shadow-lg h-100",
                        ),
                        span=12,
                        md=4,
                        cls="mb-4",
                    )
                    for i in range(3)
                ],
                cls="g-4",
            ),
            cls="py-5",
            id="portfolio",
        )
    )


# ============================================================
# TESTIMONIALS SECTION (TABS)
# ============================================================
def testimonials_section():
    return Container(
        Div(
            H2("Testimonials", cls="fw-bold mb-4"),
            Tabs(
                ("client1", "Client A", True),
                ("client2", "Client B"),
                ("client3", "Client C"),
                variant="pills",
            ),
            Div(
                TabPane(
                    P(
                        "“Outstanding work. Reliable, fast, and amazing engineering skills!” – Client A"
                    ),
                    tab_id="client1",
                    active=True,
                ),
                TabPane(
                    P("“Delivered a complete SaaS solution beyond expectations.” – Client B"),
                    tab_id="client2",
                ),
                TabPane(
                    P("“Exceptional problem-solving and system architecture.” – Client C"),
                    tab_id="client3",
                ),
                cls="tab-content p-4 rounded bg-dark mt-3",
            ),
            cls="py-5",
            id="testimonials",
        )
    )


# ============================================================
# CONTACT SECTION
# ============================================================
def contact_section():
    return Container(
        Div(
            H2("Contact Me", cls="fw-bold mb-4"),
            Alert(
                "Feel free to reach out for collaborations, projects, or hiring.",
                variant="info",
                cls="mb-4",
            ),
            Form(
                Input("name", label="Full Name", placeholder="Enter your name", required=True),
                Input(
                    "email",
                    label="Email Address",
                    input_type="email",
                    placeholder="you@example.com",
                    required=True,
                ),
                Input("subject", label="Subject", placeholder="Message subject"),
                Label("Message", cls="form-label"),
                Textarea(
                    "message",
                    placeholder="Write your message...",
                    cls="form-control mb-3",
                    rows="4",
                ),
                Button("Send Message", variant="primary", size="lg"),
                method="post",
                action="/contact",
                cls="p-4 bg-dark rounded",
            ),
            cls="py-5",
            id="contact",
        )
    )


# ============================================================
# ROUTES
# ============================================================
@app.route("/")
def home():
    return Div(
        navbar,
        hero_section(),
        about_section(),
        portfolio_section(),
        testimonials_section(),
        contact_section(),
        cls="pb-5",
    )


@app.route("/contact", methods=["POST"])
def send_message(request):
    data = request.form
    print("New Contact Message:", data)
    return Alert("Thank you! Your message was received.", variant="success")


# ============================================================
# RUN SERVER
# ============================================================
if __name__ == "__main__":
    print("🚀 Portfolio running at http://localhost:5001")
    serve()
