import webapp2
import jinja2

from google.appengine.ext import db


jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader('templates'), 
								autoescape = True)

class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))



class MainPage(MainHandler):
	def get(self):
		self.render('main.html')


class Sheet(MainHandler):
	def get(self):
		self.render('Sheet.html')


class PostSheet(db.Model):

	length = db.FloatProperty(required = True)
	breadth = db.FloatProperty(required = True)
	gsm = db.FloatProperty(required = True)
	rulingRatePerkg = db.FloatProperty(required = True)
	sheetRatePerkg = db.FloatProperty(required = True)
	weightPerReam = db.FloatProperty(required = True)
	rulingCostPerReam = db.FloatProperty(required = True)
	sheetCostPerReam = db.FloatProperty(required = True)
	finalCostPerReam = db.FloatProperty(required = True)


class addSheet(MainHandler):
	def get(self):
		self.render('addSheet.html')

	def post(self):
		length = self.request.get('length')
		length = float(length)
		breadth = self.request.get('breadth')
		breadth = float(breadth)
		gsm = self.request.get('gsm')
		gsm = float(gsm)
		rulingRatePerkg = self.request.get('rpk')
		rulingRatePerkg = float(rulingRatePerkg)
		sheetRatePerkg = self.request.get('scpk')
		sheetRatePerkg = float(sheetRatePerkg)

		weightPerReam = (length * breadth * gsm) / 20000
		rulingCostPerReam = weightPerReam * rulingRatePerkg
		sheetCostPerReam = weightPerReam * sheetRatePerkg
		finalCostPerReam = rulingCostPerReam + sheetCostPerReam

		p = PostSheet(length = length, breadth = breadth, gsm = gsm, rulingRatePerkg = rulingRatePerkg, sheetRatePerkg = sheetRatePerkg,
						 weightPerReam = weightPerReam, rulingCostPerReam = rulingCostPerReam, sheetCostPerReam = sheetCostPerReam,
						  finalCostPerReam = finalCostPerReam)
		p.put()

		self.redirect('Sheet/addSheet/key=%s' % str(p.key().id()))


class added(MainHandler):
	def get(self):
		self.render('added.html')



class displaySheet(MainHandler):
	def get(self):
		sheets = greetings = PostSheet.all()
		self.render('displaySheet.html', sheets = sheets)


class deleteSheet(MainHandler):
	def get(self):
		self.render('getkey.html')


	def post(self):
		Sheet_id = self.request.get('getKey')
		Sheet_id =  long(Sheet_id)
		delentity = PostSheet.get_by_id(Sheet_id)
		delkey = delentity.key()
		db.delete(delkey)
		self.redirect('Sheet/deleteSheet/itemhasbeendeleted')


class updateSheet(MainHandler):

	def get(self):
		self.render('getkey.html')


	def post(self):
		updatekey = self.request.get('getKey')
		updateEntity = PostSheet.get(db.Key.from_path('PostSheet', int(updatekey)))
		self.render('updateSheet.html', updateLength = updateEntity.length, updateBreadth = updateEntity.breadth, updateGsm = updateEntity.gsm,
										 updateRpk = updateEntity.rulingRatePerkg, updateScpk = updateEntity.sheetRatePerkg, updatekey = updatekey)



class updateSheetValue(MainHandler):

	def post(self):
		length = self.request.get('length')
		length = float(length)
		breadth = self.request.get('breadth')		
		breadth = float(breadth)
		gsm = self.request.get('gsm')
		gsm = float(gsm)
		updatekey = self.request.get('updatekey')

		rulingRatePerkg = self.request.get('rpk')
		rulingRatePerkg = float(rulingRatePerkg)
		sheetRatePerkg = self.request.get('scpk')		
		sheetRatePerkg = float(sheetRatePerkg)
		weightPerReam = (length * breadth * gsm) / 20000
		rulingCostPerReam = weightPerReam * rulingRatePerkg
		sheetCostPerReam = weightPerReam * sheetRatePerkg					
		finalCostPerReam = rulingCostPerReam + sheetCostPerReam


		updateEntity = PostSheet.get(db.Key.from_path('PostSheet', int(updatekey)))
		updateEntity.length = length
		updateEntity.breadth = breadth			
		updateEntity.gsm = gsm
		updateEntity.rulingRatePerkg = rulingRatePerkg
		updateEntity.sheetRatePerkg = sheetRatePerkg			
		updateEntity.weightPerReam = weightPerReam
		updateEntity.rulingCostPerReam = rulingCostPerReam
		updateEntity.sheetCostPerReam = sheetCostPerReam			
		updateEntity.finalCostPerReam = finalCostPerReam
		updateEntity.put()

		self.redirect('/Sheet/updateSheet/itemHasBeenUpdated')




class Cover(MainHandler):
	def get(self):
		self.render('Cover.html')

class PostCover(db.Model):

	length = db.FloatProperty(required = True)
	breadth = db.FloatProperty(required = True)
	gsm = db.FloatProperty(required = True)
	costcoverSheetperkg = db.FloatProperty(required = True)
	PrintingCostperReam = db.FloatProperty(required = True)
	LaminationDiscount = db.FloatProperty(required = True)
	SheetWeightperReam = db.FloatProperty(required = True)
	CostPerReam = db.FloatProperty(required = True)
	LaminationperSheet = db.FloatProperty(required = True)
	LaminationperReamwdis = db.FloatProperty(required = True)
	finalCostCoverperReam = db.FloatProperty(required = True)
	finalCostCoverperSheet = db.FloatProperty(required = True)



class addCover(MainHandler):
	def get(self):
		self.render('addCover.html')

	def post(self):
		length = self.request.get('length')
		length = float(length)
		breadth = self.request.get('breadth')
		breadth = float(breadth)
		gsm = self.request.get('gsm')
		gsm = float(gsm)
		costcoverSheetperkg = self.request.get('ccspk')
		costcoverSheetperkg = float(costcoverSheetperkg)
		PrintingCostperReam = self.request.get('pcpr')
		PrintingCostperReam = float(PrintingCostperReam)
		LaminationDiscount = self.request.get('ld')
		LaminationDiscount = float(LaminationDiscount)
		LaminationDiscount = LaminationDiscount/100

		SheetWeightperReam = (length * breadth * gsm)/20000
		CostPerReam = costcoverSheetperkg * SheetWeightperReam
		LaminationperSheet = ((length * breadth)/(2.54 * 2.54))/100
		LaminationperReamwdis = LaminationperSheet * 500 * (1 - LaminationDiscount)
		finalCostCoverperReam = CostPerReam + PrintingCostperReam + LaminationperReamwdis
		finalCostCoverperSheet = finalCostCoverperReam/500


		p = PostCover(length = length, breadth = breadth, gsm = gsm, costcoverSheetperkg = costcoverSheetperkg, PrintingCostperReam = PrintingCostperReam,
		 				LaminationDiscount = LaminationDiscount, SheetWeightperReam = SheetWeightperReam, CostPerReam = CostPerReam, 
		 				LaminationperSheet = LaminationperSheet, LaminationperReamwdis = LaminationperReamwdis, 
		 				finalCostCoverperReam = finalCostCoverperReam, finalCostCoverperSheet = finalCostCoverperSheet)

		p.put()

		self.redirect('Cover/addCover/%s' % str(p.key().id()))


class displayCover(MainHandler):
	def get(self):
		covers = PostCover.all()
		self.render('displayCover.html', covers = covers)



class deleteCover(MainHandler):
	def get(self):
		self.render('getkey.html')


	def post(self):
		Cover_id = self.request.get('getKey')
		Cover_id =  long(Cover_id)
		delentity = PostCover.get_by_id(Cover_id)
		delkey = delentity.key()
		db.delete(delkey)
		self.redirect('Cover/deleteCover/itemhasbeendeleted')




class updateCover(MainHandler):
	def get(self):
		self.render('getkey.html')

	def post(self):
		updatekey = self.request.get('getKey')
		updateEntity = PostCover.get(db.Key.from_path('PostCover', int(updatekey)))
		self.render('updateCover.html', length = updateEntity.length, breadth = updateEntity.breadth, gsm = updateEntity.gsm, ccspk = updateEntity.costcoverSheetperkg,
											pcpr = updateEntity.PrintingCostperReam, ld = (updateEntity.LaminationDiscount*100), updatekey = updatekey)


class updateCoverValue(MainHandler):
	def post(self):
		length = self.request.get('length')
		length = float(length)
		breadth = self.request.get('breadth')
		breadth = float(breadth)
		gsm = self.request.get('gsm')
		gsm = float(gsm)
		costcoverSheetperkg = self.request.get('ccspk')
		costcoverSheetperkg = float(costcoverSheetperkg)
		PrintingCostperReam = self.request.get('pcpr')
		PrintingCostperReam = float(PrintingCostperReam)
		LaminationDiscount = self.request.get('ld')
		LaminationDiscount = float(LaminationDiscount)
		LaminationDiscount = LaminationDiscount/100
		updatekey = self.request.get('updatekey')

		SheetWeightperReam = (length * breadth * gsm)/20000
		CostPerReam = costcoverSheetperkg * SheetWeightperReam
		LaminationperSheet = ((length * breadth)/(2.54 * 2.54))/100
		LaminationperReamwdis = LaminationperSheet * 500 * (1 - LaminationDiscount)
		finalCostCoverperReam = CostPerReam + PrintingCostperReam + LaminationperReamwdis
		finalCostCoverperSheet = finalCostCoverperReam/500

		updateEntity = PostCover.get(db.Key.from_path('PostCover', int(updatekey)))
		updateEntity.length = length
		updateEntity.breadth = breadth			
		updateEntity.gsm = gsm
		updateEntity.costcoverSheetperkg = costcoverSheetperkg
		updateEntity.PrintingCostperReam = PrintingCostperReam
		updateEntity.LaminationDiscount = LaminationDiscount
		updateEntity.SheetWeightperReam = SheetWeightperReam
		updateEntity.CostPerReam = CostPerReam
		updateEntity.LaminationperSheet = LaminationperSheet
		updateEntity.LaminationperReamwdis = LaminationperReamwdis
		updateEntity.finalCostCoverperReam = finalCostCoverperReam
		updateEntity.finalCostCoverperSheet = finalCostCoverperSheet
		updateEntity.put()

		self.redirect('/Cover/updateCover/itemHasBeenUpdated')











class Product(MainHandler):
	def get(self):
		self.render('Product.html')



class PostProduct(db.Model):
	productName = db.StringProperty(required = True)
	productNumber = db.IntegerProperty(required = True)
	pages = db.IntegerProperty(required = True)
	length = db.FloatProperty(required = True)
	breadth = db.FloatProperty(required = True)
	pSheetId = db.StringProperty(required = True)
	pagesPerSheet = db.FloatProperty(required = True)
	cSheetId = db.StringProperty(required = True)
	coverPerSheet = db.FloatProperty(required = True)
	miscellaneousCost = db.FloatProperty(required = True)
	labourCost = db.FloatProperty(required = True)
	profit = db.FloatProperty(required = True)
	costofSheetperReam = db.FloatProperty(required = True)
	costofCoverSheetperReam = db.FloatProperty(required = True)
	costofPaperinProduct = db.FloatProperty(required = True)
	costofCoverinProduct = db.FloatProperty(required = True)
	manufactureCost = db.FloatProperty(required = True)
	afterProfit = db.FloatProperty(required = True)
	productPrice = db.FloatProperty(required = True)
	sellingPricePerGross = db.FloatProperty(required = True)



class addProduct(MainHandler):
	def get(self):
		self.render('addProduct.html')

	def post(self):
		productName = self.request.get('product_name')
		productName = str(productName)
		productNumber = self.request.get('product_no')
		productNumber = long(productNumber)
		pages = self.request.get('pages')
		pages = int(pages)
		length = self.request.get('length')
		length = float(length)
		breadth = self.request.get('breadth')
		breadth = float(breadth)
		pSheetId = self.request.get('psid')
		#pSheetId = float(pSheetId)
		pagesPerSheet = self.request.get('pps')
		pagesPerSheet = float(pagesPerSheet)
		cSheetId = self.request.get('csid')
		#cSheetId = float(cSheetId)
		coverPerSheet = self.request.get('cpcs')
		coverPerSheet = float(coverPerSheet)
		miscellaneousCost = self.request.get('ms')
		miscellaneousCost = float(miscellaneousCost)
		labourCost = self.request.get('lc')
		labourCost = float(labourCost)
		profit = self.request.get('profit')
		profit = float(profit)
		profit = profit/100



		coverEntity = PostCover.get(db.Key.from_path('PostCover', int(cSheetId)))
		costofCoverSheetperReam = coverEntity.finalCostCoverperReam

		sheetEntity = PostSheet.get(db.Key.from_path('PostSheet', int(pSheetId)))
		costofSheetperReam = sheetEntity.finalCostPerReam


		costofPaperinProduct = (costofSheetperReam * pages)/(500 * pagesPerSheet)
		costofCoverinProduct = (costofCoverSheetperReam)/(500 * coverPerSheet)
		manufactureCost = costofPaperinProduct + costofCoverinProduct + labourCost + miscellaneousCost
		afterProfit = manufactureCost * (1 + profit)
		productPrice = afterProfit * 1.13
		sellingPricePerGross = productPrice * 144

		p = PostProduct(productName = productName, productNumber = productNumber, pages = pages, length = length, breadth = breadth, pSheetId = pSheetId,
						pagesPerSheet = pagesPerSheet, cSheetId = cSheetId, coverPerSheet = coverPerSheet, miscellaneousCost = miscellaneousCost, 
						 labourCost = labourCost,  profit = profit, costofSheetperReam = costofSheetperReam, costofCoverSheetperReam = costofCoverSheetperReam,
						 costofPaperinProduct = costofPaperinProduct, costofCoverinProduct = costofCoverinProduct, manufactureCost = manufactureCost, 
						 afterProfit = afterProfit, productPrice = productPrice, sellingPricePerGross = sellingPricePerGross)

		p.put()
		self.redirect('Product/addProduct/%s' % str(p.key().id()))



class displayProduct(MainHandler):
	def get(self):
		products = PostProduct.all()
		self.render('displayProduct.html', products = products)



class deleteProduct(MainHandler):
	def get(self):
		self.render('getkey.html')


	def post(self):
		Product_id = self.request.get('getKey')
		Product_id =  long(Product_id)
		delentity = PostProduct.get_by_id(Product_id)
		delkey = delentity.key()
		db.delete(delkey)
		self.redirect('Product/deleteProduct/itemhasbeendeleted')




class updateProduct(MainHandler):
	def get(self):
		self.render('getkey.html')

	def post(self):
		updatekey = self.request.get('getKey')
		updateEntity = PostProduct.get(db.Key.from_path('PostProduct', int(updatekey)))
		self.render('updateProduct.html', product_name = updateEntity.productName, product_no = updateEntity.productNumber, pages = updateEntity.pages, length = updateEntity.length,
											breadth = updateEntity.breadth, psid = updateEntity.pSheetId, pps = updateEntity.pagesPerSheet, csid = updateEntity.cSheetId, 
											cpcs = updateEntity.coverPerSheet, ms = updateEntity.miscellaneousCost, lc = updateEntity.labourCost, profit = (updateEntity.profit * 100), 
											updatekey = updatekey)

class updateProductValue(MainHandler):
	def post(self):
		productName = self.request.get('product_name')
		productName = str(productName)
		productNumber = self.request.get('product_no')
		productNumber = long(productNumber)
		pages = self.request.get('pages')
		pages = int(pages)
		length = self.request.get('length')
		length = float(length)
		breadth = self.request.get('breadth')
		breadth = float(breadth)
		pSheetId = self.request.get('psid')
		#pSheetId = float(pSheetId)
		pagesPerSheet = self.request.get('pps')
		pagesPerSheet = float(pagesPerSheet)
		cSheetId = self.request.get('csid')
		#cSheetId = float(cSheetId)
		coverPerSheet = self.request.get('cpcs')
		coverPerSheet = float(coverPerSheet)
		miscellaneousCost = self.request.get('ms')
		miscellaneousCost = float(miscellaneousCost)
		labourCost = self.request.get('lc')
		labourCost = float(labourCost)
		profit = self.request.get('profit')
		profit = float(profit)
		profit = profit/100
		updatekey = self.request.get('updatekey')


		coverEntity = PostCover.get(db.Key.from_path('PostCover', int(cSheetId)))
		costofCoverSheetperReam = coverEntity.finalCostCoverperReam

		sheetEntity = PostSheet.get(db.Key.from_path('PostSheet', int(pSheetId)))
		costofSheetperReam = sheetEntity.finalCostPerReam


		costofPaperinProduct = (costofSheetperReam * pages)/(500 * pagesPerSheet)
		costofCoverinProduct = (costofCoverSheetperReam)/(500 * coverPerSheet)
		manufactureCost = costofPaperinProduct + costofCoverinProduct + labourCost + miscellaneousCost
		afterProfit = manufactureCost * (1 + profit)
		productPrice = afterProfit * 1.13
		sellingPricePerGross = productPrice * 144




		updateEntity = PostProduct.get(db.Key.from_path('PostProduct', int(updatekey)))
		updateEntity.productName = productName
		updateEntity.productNumber = productNumber
		updateEntity.pages = pages
		updateEntity.length = length
		updateEntity.breadth = breadth
		updateEntity.pSheetId = pSheetId
		updateEntity.pagesPerSheet = pagesPerSheet
		updateEntity.cSheetId = cSheetId
		updateEntity.coverPerSheet = coverPerSheet
		updateEntity.miscellaneousCost = miscellaneousCost 
		updateEntity.labourCost = labourCost
		updateEntity.profit = profit
		updateEntity.costofSheetperReam = costofSheetperReam
		updateEntity.costofCoverSheetperReam = costofCoverSheetperReam
		updateEntity.costofPaperinProduct = costofPaperinProduct
		updateEntity.costofCoverinProduct = costofCoverinProduct
		updateEntity.manufactureCost = manufactureCost 
		updateEntity.afterProfit = afterProfit
		updateEntity.productPrice = productPrice
		updateEntity.sellingPricePerGross = sellingPricePerGross
		updateEntity.put()

		self.redirect('Product/updateProduct/itemHasBeenUpdated')








app = webapp2.WSGIApplication([
    							('/', MainPage),
    							('/Sheet',Sheet),
    							('/Cover',Cover),
    							('/Product',Product),
    							('/Sheet/addSheet', addSheet),
    							('/Sheet/displaySheet', displaySheet),
    							('/Sheet/deleteSheet', deleteSheet),
    							('/Sheet/updateSheet', updateSheet),
    							('/updateSheetValue', updateSheetValue),
    							('/Cover/addCover', addCover),
    							('/Cover/displayCover', displayCover),
    							('/Cover/deleteCover', deleteCover),
    							('/Cover/updateCover', updateCover),
    							('/updateCoverValue', updateCoverValue),
    							('/Product/addProduct', addProduct),
    							('/Product/displayProduct', displayProduct),
    							('/Product/deleteProduct', deleteProduct),
    							('/Product/updateProduct', updateProduct),
    							('/updateProductValue', updateProductValue)
    							], 
    							debug=True)
