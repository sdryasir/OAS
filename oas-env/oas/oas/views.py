from django.shortcuts import render
from browseproduct.models import cards
from django.core.paginator import Paginator 

def home(request):
    data = {
        "products":[
            {
            "title":"Alarm Clock 1990’s",
            "text":"Current Bid:",
            "amount":"507.0$",
            "button":"Place A Bid",
            "img":" ",
            
            },

            {
                "title":"Couple Wedding Ring",
            "text":"Current Bid:",
            "amount":"6,100.1$",
            "button":"Place A Bid",
            "img":" ",
            

            },

            {
                "title":"Premium 1998 Typewriter",
            "text":"Current Bid:",
            "amount":"574.0$",
            "button":"Place A Bid",
            "img":" ",
            
            },

            {
                "title":"Macbook Pro 2018",
            "text":"Current Bid:",
            "amount":"12,761.0$",
            "button":"Place A Bid",
            "img":" ",
            
            },

            {
                "title":"Black Analogue Watch",
            "text":"Current Bid:",
            "amount":"2,104.0$",
            "button":"Place A Bid",
            "img":" ",
            
            },

            {
                "title":"Ford Shelby White Car",
            "text":"Current Bid:",
            "amount":"20,414.0$",
            "button":"Place A Bid",
            "img":" ",
            
            }
            ],
            "products2":[
                {
                    "tag":"Accessories",
                    "title":"Couple Wedding Ring",
                    "text":"Current Bid:",
                    "amount":"6,100.1$",
                    "button":"View Details",
                    "img":" "
                },

                {
                    "tag":"Accessories,Electonic",
                    "title":"Alarm Clock 1990’s",
                    "text":"Current Bid:",
                    "amount":"507.0$",
                    "button":"View Details",
                    "img":" "
                },

                {
                    "tag":"Accessories,Electronics",
                    "title":"Premium 1998 Typewriter",
                    "text":"Current Bid:",
                    "amount":"574.0$",
                    "button":"View Details",
                    "img":" "
                }
            ],
            "products3":[
                {
                    "title":"An Introvert’s Guide to Be Successful at Work",
                    "img":" D:\oas\oas-env\oas\static\pic1.jpg",
                    "dpimg":" ",
                    "btext":"November 3,2022",
                    "ctext":"1 comments",
                    "text":"Egens Lab"

                },

                {
                    "title":"Why You Should (Often) Pay More for Links",
                    "img":" ",
                    "dpimg":" ",
                    "btext":"November 3,2022",
                    "ctext":"0 comments",
                    "text":"Egens Lab"


                },

                {
                    "title":"David Droga Still Has Faith in Online Creative.",
                    "img":" ",
                    "dpimg":" ",
                    "btext":"October 9,2022",
                    "ctext":"0 comments",
                    "text":"Egens Lab"


                },
            ]
    }
    return render(request,'task1.html', data )

def browseproduct(request):
    cardsdata = cards.objects.all()
    bot = Paginator(cardsdata,5)
    page = request.GET.get('page',1)
    page_obj = bot .get_page(page)
    

    totalpages =  [x+1 for x in range( bot.num_pages)]
    
    
    data = {
        "products":page_obj,
        "totalpages":totalpages 
    }
    return render(request,'browse.html',data)

