import scrapy
from scrapy import Request



class COLSpider(scrapy.Spider):
    name = 'col'
    RegionID = 4
    start_urls = ['http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=3&RegionName=Mumbai'

                  ]

    #def parse(self, response):
        #institute = response.css('#ctl00_ContentPlaceHolder1_gvInstituteList a ::attr(href)').get()
        #link = response.urljoin(institute)
        #yield Request(url=link, callback=self.parse_info)


    def parse(self, response):
        all_institutes = response.css('#ctl00_ContentPlaceHolder1_gvInstituteList a ::attr(href)').getall()
        for institute in all_institutes:
            link = response.urljoin(institute)
            yield Request(url=link, callback=self.parse_info)


    #def parse_summary(self, response):
        #link = response.urljoin('frmInstituteSummary.aspx?InstituteCode=3001')
        #yield Request(url=link, callback=self.parse_info)

    def parse_info(self, response):
        Institute_name = response.css('#ctl00_ContentPlaceHolder1_lblInstituteNameEnglish ::text').get()
        Region_type = response.css('#ctl00_ContentPlaceHolder1_lblRegionType ::text').get()
        Institute_address = response.css('#ctl00_ContentPlaceHolder1_lblAddressEnglish ::text').get()
        District = response.css('#ctl00_ContentPlaceHolder1_lblDistrict ::text').get()
        Pincode = response.css('#ctl00_ContentPlaceHolder1_lblPincode ::text').get()
        Web_address = response.css('#ctl00_ContentPlaceHolder1_lblWebAddress ::text').get()
        Email_address = response.css('#ctl00_ContentPlaceHolder1_lblEMailAddress ::text').get()
        Principal_name = response.css('#ctl00_ContentPlaceHolder1_lblPrincipalNameEnglish ::text').get()
        Office_contact = response.css('#ctl00_ContentPlaceHolder1_lblOfficePhoneNo ::text').get()
        personal_contact = response.css('#ctl00_ContentPlaceHolder1_lblPersonalPhoneNo ::text').get()
        Registrar_name = response.css('#ctl00_ContentPlaceHolder1_lblRegistrarNameEnglish ::text').get()
        Autonomy_status = response.css('#ctl00_ContentPlaceHolder1_lblStatus2 ::text').get()


        item = {
            'Institute_name' : Institute_name,
            'Region_type' : Region_type,
            'Institute_address' : Institute_address,
            'District' : District,
            'Pincode' : Pincode,
            'Web_address' : Web_address,
            'Email_address' : Email_address,
            'Principal_name' : Principal_name,
            'Office_contact' : Office_contact,
            'personal_contact' : personal_contact,
            'Registrar_name' : Registrar_name,
            'Autonomy_status' : Autonomy_status






        }
        yield item


        next_page = 'http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=' +str(COLSpider.RegionID) + '&RegionName=Pune'
        if COLSpider.RegionID <= 6:
            COLSpider.RegionID += 1

            yield response.follow(next_page, callback = self.parse)




