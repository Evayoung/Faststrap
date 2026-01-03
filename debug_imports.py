try:
    print("Attempting imports...")
    from faststrap import (
        ConfirmDialog,
        EmptyState,
        Figure,
        FileInput,
        Hero,
        Popover,
        StatCard,
        Tooltip,
    )

    print("Imports successful!")

    # Quick instantiation check
    print("Instantiating components...")
    f = FileInput("test")
    t = Tooltip("T", "Child")
    p = Popover("T", "C", "Child")
    fig = Figure("img.jpg")
    es = EmptyState(title="Empty")
    sc = StatCard("Stat", "100")
    cd = ConfirmDialog("Confirm?")
    h = Hero("Hero")
    print("Instantiation successful!")

except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
    import traceback

    traceback.print_exc()
