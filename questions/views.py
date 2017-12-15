from django.shortcuts import render
from scrapy_project.spiders.stackoverflow import StackoverflowSpider
from django.http import HttpResponseRedirect,HttpResponse
from scrapy_project.pipelines import ScrapyProjectPipeline
from questions.models import Questions
from questions.forms import PostForm
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
def list_view(request):
    items = Questions.objects.all()
    return render(request, 'questions/indes.html', {
        'form': items
    })


def start_proccess(request):
        item = ScrapyProjectPipeline.process_item
        items = Questions.objects.all()

        # os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "whereyourscrapysettingsare")



def send_form(request):
    if request.method == 'POST':
        s=StackoverflowSpider()
        s.start_spider()
        return HttpResponse('So good')
    else:
        form = PostForm()
        return render(request, 'questions/form.html', {
            'form': form
        })
    # Create your views here.
