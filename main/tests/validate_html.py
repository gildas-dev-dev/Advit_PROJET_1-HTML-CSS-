from pathlib import Path


def main() -> None:
    html_path = Path(__file__).resolve().parents[1] / "index.html"
    contents = html_path.read_text(encoding="utf-8")

    required_snippets = [
        '<html lang="fr">',
        "<title>accueil</title>",
        "</footer>",
    ]

    missing = [snippet for snippet in required_snippets if snippet not in contents]
    if missing:
        formatted = "\n".join(f"- {snippet}" for snippet in missing)
        raise SystemExit(
            "HTML validation failed. Missing required snippets:\n" + formatted
        )

    print("HTML validation passed.")


if __name__ == "__main__":
    main()
