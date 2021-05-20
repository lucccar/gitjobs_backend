import constants as constants
from scrapy.selector import Selector
import requests


GIT_JOBS_URI="https://jobs.github.com/positions?utf8=✓&description={}&location={}"

def access_git_jobs(location, description):

    uri = GIT_JOBS_URI.format(description, location)

    html_text = ""
    response = requests.get(uri)
    selection = Selector(response=response).xpath('//section')
    for html in selection:

        html_text = html.extract()

    return html_text
