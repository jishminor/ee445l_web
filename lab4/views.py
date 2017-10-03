from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import VoltageSample
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart




# Create your views here.
def index(request):
    voltage_data = VoltageSample.objects.all()
    template = loader.get_template('index.html')
    context = {
        'voltage_data': voltage_data
    }
    return HttpResponse(template.render(context, request))

def receiveData(request):
    if 'q' in request.GET:
        try:
            v = VoltageSample()
            if 'name' in request.GET:
                v.name = request.GET['name']
            i = 0
            if 'vals' in request.GET:
                values_string = request.GET['vals']
                values = values_string.split(',')
                values_floats = []
                for val in values:
                    values_floats.append(float(val))
                v.data = values_floats
                v.save()
                print("Saved new object")
        except:
            print("Received request, error in parsing")
    else:
        print("Received request, but no query")

    response = HttpResponse()
    response.write("hit")
    return response

def plots(request, data_id):
    vs = VoltageSample.objects.all().filter(id=data_id)[0]
    if vs:
        data = [['Time(seconds)', 'Voltage']]
        samples = []
        i = 0
        for d in vs.data:
            val = [str(i), d]
            samples.append(val)
            i = i + 1
            data.append(val)
    # DataSource object
    data_source = SimpleDataSource(data=data)
    # Chart object
    options = {'title': 'Voltage vs Time',
               'vAxis': {'title': 'Volts'},
               'hAxis': {'title': 'Seconds', 'minValue': 0, 'viewWindowMode': 'maximized'}
    }
    chart = LineChart(data_source, height=500, width=1000, options=options)
    context = {'chart': chart}
    return render(request, 'plot.html', context)



