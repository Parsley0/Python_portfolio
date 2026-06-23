from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import ContactMessage

PROJECTS = [
    {
        'title': 'Sem-Sync',
        'description': (
            'Sem-Sync is a student-focused academic management platform designed to help '
            'learners organize and synchronize their semester activities in one place. The '
            'system streamlines task tracking, course schedules, deadlines, assignments, and '
            'academic progress to improve productivity and time management for university students.'
        ),
        'live_url': 'https://semsync.brian-kinyua.me/',
        'github_url': 'https://github.com/still-figuring/Sem-Sync',
        'tech_stack': [
            'React', 'Node.js', 'Express', 'Firebase',
            'Typescript', 'Tailwind CSS', 'Kotlin',
        ],
    },
    {
        'title': 'Pathfinder KE',
        'description': (
            'Pathfinder-KE is an interactive career guidance simulation game built to help '
            'students explore different professions, understand required skills and education '
            'paths, and make informed career decisions through gameplay, challenges, and '
            'real-world scenarios.'
        ),
        'live_url': 'https://pathfinder.jhubafrica.com/',
        'github_url': 'https://github.com/Brikita/Pathfinder-ke',
        'tech_stack': [
            'React', 'Node.js', 'JavaScript', 'Tailwind CSS', 'C#', 'Unity',
        ],
    },
    {
        'title': 'Wellness Tracker',
        'description': (
            'Wellness Tracker is a web application designed to help users monitor their '
            'physical and mental health, set goals, and maintain a healthy lifestyle through '
            'personalized tracking and insights.'
        ),
        'live_url': '#',
        'github_url': 'https://github.com/Parsley0/plp-mern-final-project',
        'tech_stack': [
            'React', 'Node.js', 'Express', 'MongoDB', 'JavaScript', 'Tailwind CSS',
        ],
    },
]

ABOUT_PARAGRAPHS = [
    (
        'I focus on full-stack web development, mobile applications, and interactive games. '
        'From designing intuitive user interfaces to building robust backend systems, I enjoy '
        'working across the entire development lifecycle to bring ideas to life.'
    ),
    (
        'With a strong foundation in computer science and a passion for learning new '
        'technologies, I am dedicated to delivering high-quality software solutions. I thrive '
        'on collaboration, problem-solving, and continuously improving my skills to stay at '
        'the forefront of innovation.'
    ),
    (
        'I am always excited to connect with fellow developers, explore new opportunities, '
        'and contribute to projects that make a meaningful impact.'
    ),
]

HIGHLIGHTS = [
    {
        'title': 'Clean Code',
        'description': (
            'I write clean, maintainable code that follows best practices and design patterns.'
        ),
        'icon': 'code',
    },
    {
        'title': 'Performance Optimization',
        'description': (
            'I optimize applications for speed and efficiency, ensuring a smooth user experience.'
        ),
        'icon': 'cpu',
    },
    {
        'title': 'Collaboration',
        'description': (
            'I work well in team environments, communicating effectively and contributing '
            'to group success.'
        ),
        'icon': 'users',
    },
    {
        'title': 'Fast Development',
        'description': (
            'I leverage modern tools and techniques to deliver high-quality software quickly '
            'and efficiently.'
        ),
        'icon': 'zap',
    },
]

EXPERIENCE = [
    {
        'role': 'Game Developer Intern',
        'organization': 'JHUB Africa',
        'location': 'Juja, Kenya',
        'period': 'May 2025 — September 2025',
        'description': (
            'During my internship at JHUB Africa, I had the opportunity to work on an exciting '
            'project focused on developing a 3D game using Unity and C#. My role involved '
            'collaborating with a team of developers to design and implement game mechanics, '
            'create interactive environments, and optimize performance. I gained hands-on '
            'experience in game development, including scripting, level design, and debugging. '
            'This internship allowed me to apply my programming skills in a real-world setting '
            'while also fostering creativity and teamwork.'
        ),
    },
]


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            return redirect(f"{reverse('home')}?submitted=1")
    else:
        form = ContactForm()

    submitted = request.GET.get('submitted') == '1'

    context = {
        'name': 'Parsley Kabuthi Njoroge',
        'short_name': 'Parsley Njorge',
        'role_badge': 'Software Developer — Fullstack Developer',
        'hero_heading_teal': 'Building Tools',
        'hero_heading_white': 'That Make',
        'hero_heading_italic': 'Complex Ideas Simple.',
        'hero_intro': (
            'Hi, I\'m <strong>Parsley Njoroge</strong> — a passionate computer science student '
            'at Jomo Kenyatta University of Agriculture and Technology. I specialize in '
            'Fullstack development and Mobile app development.'
        ),
        'university': 'Jomo Kenyatta University of Agriculture and Technology',
        'about_label': 'About Me',
        'about_heading_teal': 'Building the future,',
        'about_heading_italic': 'one line of code at a time.',
        'about_paragraphs': ABOUT_PARAGRAPHS,
        'highlights': HIGHLIGHTS,
        'experience_label': 'Career Journey',
        'experience_heading_teal': 'Experience that are',
        'experience_heading_italic': 'shaping my path in tech.',
        'experience_intro': (
            'I\'ve gained hands-on experience through academic, personal, and collaborative '
            'projects that continue to shape my growth as a developer and problem solver.'
        ),
        'experience': EXPERIENCE,
        'projects': PROJECTS,
        'contact_label': 'Get In Touch',
        'contact_heading_teal': 'Let\'s Connect and Create',
        'contact_heading_italic': 'something amazing together.',
        'contact_intro': (
            'Whether you have a question, want to collaborate, or just want to say hi, feel '
            'free to reach out. I\'m always open to new opportunities and connections.'
        ),
        'email': 'nparsley433@gmail.com',
        'phone': '+254 719432950',
        'availability_text': (
            'As a student developer, I\'m always looking for opportunities to learn, '
            'collaborate, and work on meaningful projects that help me grow in tech.'
        ),
        'cv_url': '#',
        'github_url': '#',
        'linkedin_url': '#',
        'contact_form': form,
        'form_submitted': submitted,
    }
    return render(request, 'portfolio/home.html', context)


def download_cv(request):
    cv_path = settings.BASE_DIR / 'portfolio' / 'static' / 'portfolio' / 'cv' / "Parsley's Resume.pdf"
    if not cv_path.exists():
        raise Http404('CV not found.')
    response = FileResponse(open(cv_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Parsleys_Resume.pdf"'
    return response
