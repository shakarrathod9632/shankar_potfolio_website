from django.shortcuts import render, redirect
from .forms import ContactForm

# NOTE: We are not using Project model to keep it minimal per your request.
# Pages use static/manual content; later you can convert to model-driven content.

def index(request):
    # sample featured projects list (manual). Replace or extend as needed.
    featured = [
        {'title':'Weather Now App', 'slug':'weather-now', 'desc':'React + API, responsive dashboard'},
        {'title':'Blog Platform', 'slug':'blog-platform', 'desc':'Django + React blog with auth'},
        {'title':'E-Commerce Demo', 'slug':'ecommerce-demo', 'desc':'Stripe checkout demo and admin panel'}
    ]
    return render(request, 'portfolio/index.html', {'featured': featured})

def about(request):
    return render(request, 'portfolio/about.html')

def education(request):
    degrees = [
        {'degree':'B.Sc. in Computer Science', 'inst':'University Name', 'year':'2016 - 2019', 'detail':'Major: Software Engineering'},
        {'degree':'Diploma in Web Dev', 'inst':'Institute Name', 'year':'2020', 'detail':'Full stack foundations'}
    ]
    return render(request, 'portfolio/education.html', {'degrees': degrees})

def experience(request):
    jobs = [
        {'role':'Full Stack Developer', 'company':'ABC Solutions', 'period':'2021 - Present', 'bullets': [
            'Built REST APIs using Django REST Framework',
            'Created frontend in React and improved UX',
            'Deployed apps on Linux servers and CI/CD pipelines'
        ]},
        {'role':'Frontend Developer', 'company':'Design Co', 'period':'2019 - 2021', 'bullets': [
            'Built accessible UI components in React',
            'Improved page load times by optimizing assets'
        ]}
    ]
    return render(request, 'portfolio/experience.html', {'jobs': jobs})

def skills(request):
    # categories & skills (manual)
    skills = {
        'Frontend': [('HTML/CSS', 90), ('JavaScript', 85), ('React', 80)],
        'Backend': [('Python', 90), ('Django', 85), ('REST APIs', 82)],
        'Databases & DevOps': [('Postgres', 80), ('Docker', 70), ('NGINX', 65)]
    }
    return render(request, 'portfolio/skills.html', {'skills': skills})

def project_list(request):
    projects = [
        {'title':'Weather Now App', 'slug':'weather-now', 'desc':'Real-time weather dashboard with charts.', 'tags':['React','API']},
        {'title':'Blog Platform', 'slug':'blog-platform', 'desc':'Content publishing with admin and editor.', 'tags':['Django','React']},
        {'title':'Expense Tracker', 'slug':'expense-tracker', 'desc':'Personal expense tracker with charts.', 'tags':['Flask','JS']},
    ]
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, slug):
    # simplistic manual lookup by slug (for sample)
    projects = {
        'weather-now': {
            'title':'Weather Now App',
            'summary':'A responsive React app fetching live weather data from OpenWeatherMap.',
            'tech':['React','OpenWeatherMap API','CSS Grid'],
            'images': []
        },
        'blog-platform': {
            'title':'Blog Platform',
            'summary':'Django backend with React frontend for posts, tags and comments.',
            'tech':['Django','React','Postgres'],
            'images': []
        },
        'expense-tracker': {
            'title':'Expense Tracker',
            'summary':'Track expenses with charts and export CSV.',
            'tech':['Flask','Chart.js'],
            'images': []
        }
    }
    project = projects.get(slug)
    if not project:
        # fallback: render not-found message but still keep consistent template
        return render(request, 'portfolio/project_detail.html', {'not_found': True, 'slug': slug})
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form, 'success': success})
