import re


SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "angular",
    "vue",
    "node.js",
    "nodejs",
    "fastapi",
    "flask",
    "django",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "git",
    "github",
    "docker",
    "kubernetes",
    "rest api",
    "rest",
    "api",
    "aws",
    "azure",
    "gcp",
    "pandas",
    "numpy",
    "matplotlib",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "data analysis",
    "data science",
    "data structures",
    "algorithms",
    "oop",
    "object oriented programming",
    "spring",
    "spring boot",
    "linux",
    "bash",
    "tensorflow",
    "pytorch",
    "power bi",
    "excel"
}


def normalize_text(text: str) -> str:
    """
    Normalize text for skill detection.
    """

    text = text.lower()
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_skills(text: str) -> set[str]:
    """
    Extract known technical skills from text.
    """

    normalized_text = normalize_text(text)

    found_skills = set()

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, normalized_text):
            found_skills.add(skill)

    return found_skills
