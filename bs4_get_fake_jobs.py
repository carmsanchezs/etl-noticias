import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# the .content attribute holds raw bytes, which can be decoded better than .text
soup = BeautifulSoup(page.content, "html.parser")

# find elements by ID
results = soup.find(id="ResultsContainer")

# find elements by HTML class name, it returns an iterable
job_elements = results.find_all("div", class_="card-content")

# what about if we only need certain jobs, specifically jobs related to python
# it returns an iterable, but it only fiters the h2 elements
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# in order to access to all information, as our h2 is on the third level
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

    # Now, we need to access the link to apply
    links = job_element.find_all("a")
    # And filter only the links that contain the text "Apply"
    links_apply = [link for link in links if link.text == 'Apply']

    for link in links_apply:
        link_url = link["href"]
        print(link_url, "\n")
