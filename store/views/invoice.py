from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.invoice import Invoice
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.http import HttpResponse
from django.views.generic import View
from Eshop.utils import render_to_pdf
import datetime
from store.models.invoicepdf import Invoicepdf
from django.core.files import File
from io import BytesIO
import store.models.invoicepdf
from django.core.files.storage import FileSystemStorage

class InvoiceView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        invoices = Invoice.get_invoice_by_customer(customer)
        return render(request , 'invoice.html'  , {'invoices' : invoices})





class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        customer = request.session.get('customer')
        invoices = Invoice.get_invoice_by_customer(customer)
        obj = Invoicepdf()

        pdf = render_to_pdf('invoice.html', {'invoices' : invoices})
        # obj = Invoicepdf()
        # obj.mypdf = render_to_pdf('invoice.html', {'invoices' : invoices})
        # pdfone = File(pdf)
        # context = {'instance': obj}
        # pdf = render_to_pdf('your/pdf/template.html', context)
        filename = "Invoice/"
        mypdf = obj.mypdf.save(filename, File(BytesIO(pdf.content)))
        if mypdf:
            print("true")
        else:
            print("false")
        return HttpResponse(pdf, content_type='application/pdf')
