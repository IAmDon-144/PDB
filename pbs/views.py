from rest_framework import views
from .models import PBS, Report, SubZonal, Zonal, ComplainCenter, Fider
from .serializers import PBS_Serializer, ReportSerializer, SubZonalSerializers, ZonalSerializers, ComplainCenterSerializer, FiderSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


# ==========================All Retrive=========================


class allPBS(views.APIView):

    def get(self, request):
        pquery = PBS.objects.all()
        serializers = PBS_Serializer(pquery, many=True)
        return Response({"Pbs": serializers.data})


class allZonal(views.APIView):

    def get(self, request):
        pquery = Zonal.objects.all()
        serializers = ZonalSerializers(pquery, many=True)
        return Response({"Zonal": serializers.data})


class allSubZonal(views.APIView):

    def get(self, request):
        pquery = SubZonal.objects.all()
        serializers = SubZonalSerializers(pquery, many=True)
        return Response({"SubZonal": serializers.data})


class allComplainCenter(views.APIView):

    def get(self, request):
        pquery = ComplainCenter.objects.all()
        serializers = ComplainCenterSerializer(pquery, many=True)
        return Response({"CC": serializers.data})


class allFiders(views.APIView):
    def get(self, request,):
        pquery = Fider.objects.all()
        serializer = FiderSerializers(pquery, many=True)
        return Response({"Fiders": serializer.data})


class allReport(views.APIView):
    def get(self, request,):
        pquery = Report.objects.all()
        serializer = ReportSerializer(pquery, many=True)
        return Response({"Reports": serializer.data})


# ==========================Single Retrive=========================


class getChild(views.APIView):
    def get(self, request, pk):
        pkType = pk.split("-")[0]
        try:
            if(pkType == 'p'):
                singleItem = PBS.objects.get(id=pk)
                serializer = PBS_Serializer(singleItem, many=False)
            elif(pkType == 'z'):
                singleItem = Zonal.objects.get(id=pk)
                serializer = ZonalSerializers(singleItem, many=False)
            elif(pkType == 'sz'):
                singleItem = SubZonal.objects.get(id=pk)
                serializer = SubZonalSerializers(singleItem, many=False)
            elif(pkType == 'cc'):
                singleItem = ComplainCenter.objects.get(id=pk)
                serializer = ComplainCenterSerializer(singleItem, many=False)
            elif(pkType == 'f'):
                singleItem = Fider.objects.get(id=pk)
                serializer = FiderSerializers(singleItem, many=False)
            elif(pkType == 'r'):
                singleItem = Report.objects.get(id=pk)
                serializer = ReportSerializer(singleItem, many=False)

            return Response({"Data": serializer.data})
        except:
            return Response({"Data": "Error-Fill Up an ID"})


# class getSingleZonal(views.APIView):
#     def get(self, request, pk):
#         singleItem = Zonal.objects.get(id=pk)
#         serializer = ZonalSerializers(singleItem, many=False)
#         return Response({"Single-Zonal": serializer.data})


# class getSingleSubZonal(views.APIView):
#     def get(self, request, pk):
#         singleItem = SubZonal.objects.get(id=pk)
#         serializer = SubZonalSerializers(singleItem, many=False)
#         return Response({"Single-Sub-Zonal": serializer.data})


# class getSingleComplain(views.APIView):
#     def get(self, request, pk):
#         singleItem = ComplainCenter.objects.get(id=pk)
#         serializer = ComplainCenterSerializer(singleItem, many=False)
#         return Response({"Single-CC": serializer.data})


# class getSingleFider(views.APIView):
#     def get(self, request, pk):
#         singleItem = Fider.objects.get(id=pk)
#         serializer = FiderSerializers(singleItem, many=False)
#         return Response({"Single-Fider": serializer.data})


# class getSingleReport(views.APIView):
#     def get(self, request, pk):
#         singleItem = Report.objects.get(id=pk)
#         serializer = ReportSerializer(singleItem, many=False)
#         return Response({"Single-Report": serializer.data})

"""
ID LOCK and NOT FRIEND

https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/308595104_808457557089892_6898006815962874667_n.jpg?stp=dst-jpg_s720x720&_nc_cat=109&ccb=1-7&_nc_sid=e3f864&_nc_ohc=WOh_YA86KskAX8Rg03b&_nc_ht=scontent.fdac31-1.fna&oh=00_AT_V0QBcwDThoJ3kk9ZZs7vQRcXnP2ulLNiYtb5DhqR9qA&oe=634252C5

https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/293202937_750290582906590_2561972262227148754_n.jpg?stp=dst-jpg_s720x720&_nc_cat=106&ccb=1-7&_nc_sid=e3f864&_nc_ohc=p3Phg3L97tAAX-1NDAu&_nc_ht=scontent.fdac31-1.fna&oh=00_AT_ewovLeDXYleRPQxBPjZ52-1XRwoRplramsFMNPC-JCA&oe=634054C3












https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/287903666_1822912194719175_1036426092988782195_n.jpg?stp=dst-jpg_s720x720&_nc_cat=106&ccb=1-7&_nc_sid=e3f864&_nc_ohc=LRcYZ-gsgvAAX90gk9u&_nc_ht=scontent.fdac31-1.fna&oh=00_AT9zgH26y4Qjx53KlxN47CKUSzAG-y26grtZZ8EkivrqSQ&oe=63423079







ID LOCK BUT FRIEND

https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/277756692_344404527711550_2796659511282024012_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=e3f864&_nc_ohc=FxmZ8hkgD8UAX_v0me7&_nc_ht=scontent.fdac31-1.fna&oh=00_AT_1KRKZ1ALJpsKCMOkgsxG2ipepsgDlNaiYBMXnLONsIA&oe=63414BA4


https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/280280652_1874529222936556_7792219029729708182_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=e3f864&_nc_ohc=LTVRRuuo4ssAX9LeBby&_nc_ht=scontent.fdac31-1.fna&oh=00_AT9NV97a6CM22alQiSjUlsh9-RjzNvSz7xr82e8zndvKbw&oe=63420E1B







NORMAL PIC FRIEND

https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/309850805_3317026748579385_5642112675930474485_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=0debeb&_nc_ohc=9ywocTYZcR4AX-DqlxM&_nc_ht=scontent.fdac31-1.fna&oh=00_AT-h7EN_jE_YaT814rixlASeSvBsxMsqIsmoGgXpRkOrSA&oe=634196AD


https://www.facebook.com/photo/?fbid=3317025098579550&set=pob.100008162767509


====================================================================


https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/<first>_n.jpg?stp=dst-jpg_s720x720&_nc_cat=106&ccb=1-7&_nc_sid=e3f864&_nc_ohc=<second>_nc_ht=scontent.fdac31-1.fna&oh=00<third>



var first = 299546633_1261544301259122_6019416611082130354_

toatl = 47 (digits and Underscore)
phase 1 = 9 digits
phase 2 = 16 digits
phase 3 = 19 digits



var second = i3h6gGOIX-wAX-8Xfev&
total = 20



var third = _AT8NV8a-qxveuOELOgKyPbqKIXpclBbtVC0KkiRBIN1T7w&oe=63424823

phase 1 = 47 Char
phase 2 = 8 char 
connector = "&oe="

"""
