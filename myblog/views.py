from enum import Enum
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from pytz import timezone

# Create your views here.

class PublicationType(Enum):
    conference_paper = 1
    journal = 2
    book_chapters = 3 

__intro_links = {
    "currentPosition": ["Associate Software Engineer", "Therap (BD) Ltd"],
    "Resume": "https://drive.google.com/file/d/16R1hgl5fPDWq21f9MuO-PBDVvmVA6H-A/view?usp=sharing",
    "Google Scholar": "https://scholar.google.com/citations?user=QxAODxAAAAAJ&hl=en",
    "Research Gate": "https://www.researchgate.net/profile/Joy-Das-7",
    "GitHub": "https://github.com/JoyKrishan",
    "LinkedIn": "https://www.linkedin.com/in/joy-krishan-das-463475167/"
}

__name = "Joy Krishan Das"
__certifications = {
    "Google IT Automation with Python" : 'https://coursera.org/share/b89a58ca1d9db5d2b6978d5915e487e8',
    "Deep Learning": "https://coursera.org/share/b638d938a6c103af4c5f4a630de95bd0",
    "DeepLearning.AI TensorFlow Developer": "https://coursera.org/share/0e4e944c2c32960621184896d0e1c30a",
    "Natural Language Processing": "https://coursera.org/share/432d64aff4330d8437b31406e25cf420"
} # Name, links


__introduction =  """I'm Joy Krishan Das, and I graduated from BRAC University in 2020 with Highest Distinction. My research interest relies broadly on the area of machine learning, signal processing, and natural language processing. Previously, I worked under the supervision of  <a href = "http://home.sejong.ac.kr/~piran/"> Md. Jalil Piran </a> and  <a href = "https://www.bracu.ac.bd/about/people/amitabha-chakrabarty-phd"> Amitabha Chakraborty.</a> In addition, I was a volunteer teacher for Stanford University's Code in Place program and mentor for Natural Language Processing Specialization offered by DeepLearning.AI.<p>"""

__experience = [['Associate Software Engineer', 'Therap(BD) Ltd', 'Sep 2021 - Present','Dhaka, Bangladesh'],
                ['Lecturer (part-time)', 'Department of Computer Science and Engineering, BRAC University', 'Oct 2020 - Feb 2021', 'Dhaka, Bangladesh'],
                ['Teaching Assistant', 'Department of Computer Science and Engineering, BRAC University', 'Jan 2019 - Apr 2020', 'Dhaka, Bangladesh' ]] # a list of list 
__news = [] # list of dict
__publications = [{
    "type": PublicationType.conference_paper,
    'name': "Urban sound classification using convolutional neural network and long short term memory based on multiple features.",
    'author': ["Joy Krishan Das", "Arka Ghosh", "Abhijit Kumar Pal", "Sumit Dutta", "Amitabha Chakrabarty"],
    'proceeding': "in Proceedings <strong> 2020 Fourth International Conference On Intelligent Computing in Data Sciences (ICDS)</strong>, pp. 1-9. IEEE, 2020.",
    'paper_link': "https://ieeexplore.ieee.org/abstract/document/9268723/",
    'code_link': None
    },
    {
    "type": PublicationType.journal,
    'name': "Environmental sound classification using convolution neural networks with different integrated loss functions.",
    'author': ["Joy Krishan Das", "Md. Jalil Piran", "Amitabha Chakrabarty"],
    'proceeding': "<strong>Expert Systems</strong> 39, no. 5 (2022): e12804.",
    'paper_link': "https://onlinelibrary.wiley.com/doi/abs/10.1111/exsy.12804",
    'code_link': None
    } 
] # list of dict
__research_experience = [['Pioneer Alpha Ltd', 'Machine Learning Engineer (Intern)', 'Sep 2021 - Present']] # list of list
__education = [['BRAC University', 'B.Sc. in Computer Science and Engineering', '3.92', 'Dhaka Bangladesh', 'May 2016 - April 2020']] #university, department date, cgpa, place



user_info = {
    "intro_links": __intro_links,
    'name': __name,
    'certifications': __certifications,
    'introduction': __introduction,
    'experience': __experience,
    'news':__news,
    'publications':__publications,
    'research_experience':__research_experience,
    'education': __education,
}

def index(request):
    generate_currentTime()
    return render(request, 'myblog/index.html', user_info)


def generate_currentTime():
    tz = timezone('EST')
    user_info['updatedOn'] = datetime.now(tz).strftime("%d %b %Y %H:%M:%S") + " Eastern Time"
    