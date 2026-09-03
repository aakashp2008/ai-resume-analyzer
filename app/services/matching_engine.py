from .skill_extractor import extract_skills


def calculate_skill_score(
    resume_skills: set[str],
    required_skills: set[str]
) -> float:
    """
    Calculate percentage of required skills
    found in the resume.
    """

    if not required_skills:
        return 0.0

    matched = resume_skills.intersection(
        required_skills
    )

    score = (
        len(matched) /
        len(required_skills)
    ) * 100

    return round(score, 2)


def calculate_keyword_score(
    resume_text: str,
    job_description: str
) -> float:
    """
    Calculate a simple keyword overlap score.
    """

    resume_words = set(
        resume_text.lower().split()
    )

    job_words = set(
        job_description.lower().split()
    )

    important_words = set()

    for word in job_words:
        cleaned = word.strip(
            ".,:;!?()[]{}\"'"
        )

        if len(cleaned) >= 4:
            important_words.add(cleaned)

    if not important_words:
        return 0.0

    matched_words = (
        resume_words.intersection(
            important_words
        )
    )

    score = (
        len(matched_words) /
        len(important_words)
    ) * 100

    return round(score, 2)


def detect_experience(
    resume_text: str
) -> list[str]:
    """
    Detect common experience-related terms.
    """

    text = resume_text.lower()

    keywords = [
        "internship",
        "intern",
        "experience",
        "developer",
        "engineer",
        "project",
        "work experience"
    ]

    found = []

    for keyword in keywords:
        if keyword in text:
            found.append(keyword)

    return sorted(set(found))


def detect_education(
    resume_text: str
) -> list[str]:
    """
    Detect common education-related terms.
    """

    text = resume_text.lower()

    keywords = [
        "b.tech",
        "btech",
        "b.e",
        "bachelor",
        "degree",
        "engineering",
        "information technology",
        "computer science",
        "university",
        "college",
        "cgpa"
    ]

    found = []

    for keyword in keywords:
        if keyword in text:
            found.append(keyword)

    return sorted(set(found))


def generate_recommendations(
    missing_skills: set[str],
    experience: list[str],
    education: list[str]
) -> list[str]:
    """
    Generate simple recommendations from
    detected resume information.
    """

    recommendations = []

    if missing_skills:
        recommendations.append(
            "Consider developing or demonstrating "
            "the missing skills: "
            + ", ".join(sorted(missing_skills))
        )

    if not experience:
        recommendations.append(
            "Add relevant internships, projects, "
            "or work experience."
        )

    if not education:
        recommendations.append(
            "Clearly mention your educational "
            "qualifications."
        )

    if not recommendations:
        recommendations.append(
            "The resume contains relevant skills "
            "and supporting information for "
            "this job description."
        )

    return recommendations


def analyze_resume(
    resume_text: str,
    job_description: str
) -> dict:
    """
    Perform complete resume analysis.
    """

    resume_skills = extract_skills(
        resume_text
    )

    required_skills = extract_skills(
        job_description
    )

    matched_skills = (
        resume_skills &
        required_skills
    )

    missing_skills = (
        required_skills -
        resume_skills
    )

    skill_score = calculate_skill_score(
        resume_skills,
        required_skills
    )

    keyword_score = calculate_keyword_score(
        resume_text,
        job_description
    )

    experience = detect_experience(
        resume_text
    )

    education = detect_education(
        resume_text
    )

    ats_style_score = round(
        (skill_score * 0.70) +
        (keyword_score * 0.30),
        2
    )

    recommendations = generate_recommendations(
        missing_skills,
        experience,
        education
    )

    return {
        "ats_style_score": ats_style_score,
        "skill_match_score": skill_score,
        "keyword_score": keyword_score,
        "resume_skills": sorted(resume_skills),
        "required_skills": sorted(required_skills),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "detected_experience": experience,
        "detected_education": education,
        "recommendations": recommendations
    }
