# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
#from __future__ import unicode_literals

from django.db import models

class ArticleAds(models.Model):
    article_ads_id = models.IntegerField(primary_key=True)
    article_code = models.CharField(max_length=1024L)
    ad_manufacturer = models.CharField(max_length=128L)
    created_at = models.DateField()
    last_updated = models.DateField()
    class Meta:
        db_table = 'article_ads'

class Articles(models.Model):
    articlesid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=140L)
    datecreated = models.DateField()
    datepublish = models.DateField()
    createdby = models.CharField(max_length=45L, blank=True)
    publish = models.IntegerField()
    articletype = models.CharField(max_length=2L, blank=True)
    author = models.CharField(max_length=60L, blank=True)
    posttext = models.TextField()
    snippet = models.CharField(max_length=1024L)
    industry = models.CharField(max_length=70L, blank=True)
    keywords = models.CharField(max_length=201L, blank=True)
    class Meta:
        db_table = 'articles'

class ArticlesImages(models.Model):
    articles_images_id = models.IntegerField(primary_key=True)
    articles_id = models.IntegerField()
    imagesname = models.CharField(max_length=128L)
    last_updated = models.DateTimeField()
    width = models.CharField(max_length=10L)
    height = models.CharField(max_length=10L)
    caption = models.CharField(max_length=512L)
    class Meta:
        db_table = 'articles_images'

class ArticlesVendors(models.Model):
    articles_vendors_id = models.IntegerField(primary_key=True)
    articles_id = models.IntegerField()
    vendorname = models.CharField(max_length=100L)
    vendorlink = models.CharField(max_length=100L)
    vendordesc = models.CharField(max_length=100L)
    class Meta:
        db_table = 'articles_vendors'

class Directions(models.Model):
    directionsid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    name = models.CharField(max_length=60L)
    body = models.CharField(max_length=1000L)
    address = models.CharField(max_length=150L)
    city = models.CharField(max_length=50L)
    state = models.CharField(max_length=50L)
    zipcode = models.CharField(max_length=7L)
    date = models.DateField()
    active = models.IntegerField()
    venue = models.CharField(max_length=150L)
    class Meta:
        db_table = 'directions'

class Emaillist(models.Model):
    emaillistid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=45L, blank=True)
    lastname = models.CharField(max_length=45L, blank=True)
    email = models.CharField(max_length=45L, blank=True)
    exclusive = models.IntegerField()
    gfirstname = models.CharField(max_length=45L, blank=True)
    glastname = models.CharField(max_length=45L, blank=True)
    address = models.CharField(max_length=150L, blank=True)
    city = models.CharField(max_length=45L, blank=True)
    state = models.CharField(max_length=45L, blank=True)
    phone = models.CharField(max_length=45L, blank=True)
    zipcode = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'emaillist'

class Eventlist(models.Model):
    eventlistid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200L, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200L, blank=True)
    eventtime = models.CharField(max_length=200L, blank=True)
    description = models.CharField(max_length=2000L, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'eventlist'

class Events(models.Model):
    eventsid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    ename = models.CharField(max_length=150L)
    edate = models.DateField()
    etime = models.CharField(max_length=150L, blank=True)
    elocation = models.CharField(max_length=150L, blank=True)
    eaddress = models.CharField(max_length=150L, blank=True)
    ecity = models.CharField(max_length=150L, blank=True)
    estate = models.CharField(max_length=30L, blank=True)
    ezip = models.CharField(max_length=9L, blank=True)
    ephone = models.CharField(max_length=15L, blank=True)
    edescription = models.CharField(max_length=500L)
    class Meta:
        db_table = 'events'

class Family(models.Model):
    familyid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    name = models.CharField(max_length=80L)
    body = models.CharField(max_length=5000L)
    imagename = models.CharField(max_length=200L)
    active = models.IntegerField()
    class Meta:
        db_table = 'family'

class Fromoutoftown(models.Model):
    fromoutoftownid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    name = models.CharField(max_length=150L, blank=True)
    address = models.CharField(max_length=150L, blank=True)
    city = models.CharField(max_length=30L)
    state = models.CharField(max_length=30L)
    comment = models.CharField(max_length=500L, blank=True)
    linkname = models.CharField(max_length=150L, blank=True)
    url = models.CharField(max_length=150L, blank=True)
    imagename = models.CharField(max_length=150L, blank=True)
    class Meta:
        db_table = 'fromoutoftown'

class Fromus(models.Model):
    fromusid = models.IntegerField(primary_key=True)
    body = models.CharField(max_length=5000L)
    date = models.DateField()
    membersid = models.ForeignKey('Members')
    active = models.IntegerField()
    class Meta:
        db_table = 'fromus'

class GownsGallery(models.Model):
    gowns_galleryid = models.IntegerField(primary_key=True, db_column='gowns-galleryid') # Field renamed to remove unsuitable characters.
    productid = models.CharField(max_length=11L)
    name = models.CharField(max_length=70L)
    merchantid = models.CharField(max_length=20L)
    merchant = models.CharField(max_length=50L)
    link = models.CharField(max_length=200L)
    thumbnail = models.CharField(max_length=200L)
    bigimage = models.CharField(max_length=200L)
    price = models.CharField(max_length=20L)
    retailprice = models.CharField(max_length=20L)
    category = models.CharField(max_length=70L)
    subcategory = models.CharField(max_length=70L)
    description = models.CharField(max_length=70L)
    custom1 = models.CharField(max_length=70L)
    custom2 = models.CharField(max_length=70L)
    custom3 = models.CharField(max_length=70L)
    custom4 = models.CharField(max_length=70L)
    custom5 = models.CharField(max_length=70L)
    lastupdated = models.CharField(max_length=50L)
    status = models.CharField(max_length=50L)
    manufacturer = models.CharField(max_length=70L)
    partnumber = models.CharField(max_length=30L)
    merchantcategory = models.CharField(max_length=70L)
    merchantsubcategory = models.CharField(max_length=70L)
    shortdescription = models.CharField(max_length=40L)
    isbn = models.CharField(max_length=40L)
    class Meta:
        db_table = 'gowns-gallery'

class Guestbook(models.Model):
    guestbookid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    name = models.CharField(max_length=50L)
    date = models.DateField()
    comments = models.CharField(max_length=5000L)
    email = models.CharField(max_length=150L)
    active = models.IntegerField()
    class Meta:
        db_table = 'guestbook'

class Imagecat(models.Model):
    imagecatid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    category = models.CharField(max_length=300L, blank=True)
    description = models.CharField(max_length=200L, blank=True)
    blurb = models.CharField(max_length=200L, blank=True)
    date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'imagecat'

class Imagegal(models.Model):
    imagegalid = models.IntegerField(primary_key=True)
    imagecatid = models.IntegerField()
    membersid = models.ForeignKey('Members')
    imagename = models.CharField(max_length=100L, blank=True)
    description = models.CharField(max_length=1000L, blank=True)
    date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'imagegal'

class InvitationsWpd(models.Model):
    invitations_wpdid = models.IntegerField(primary_key=True)
    productid = models.CharField(max_length=10L)
    productname = models.CharField(max_length=75L)
    merchantid = models.CharField(max_length=15L)
    merchant = models.CharField(max_length=30L)
    link = models.CharField(max_length=150L)
    thumbnail = models.CharField(max_length=150L)
    bigimage = models.CharField(max_length=150L)
    price = models.CharField(max_length=5L)
    retail_price = models.CharField(max_length=5L)
    category = models.CharField(max_length=40L)
    subcategory = models.CharField(max_length=40L)
    description = models.CharField(max_length=1000L)
    custom1 = models.CharField(max_length=75L)
    custom2 = models.CharField(max_length=75L)
    custom3 = models.CharField(max_length=75L)
    custom4 = models.CharField(max_length=75L)
    custom5 = models.CharField(max_length=75L)
    last_updated = models.CharField(max_length=30L)
    manufacturer = models.CharField(max_length=100L)
    merchantcategory = models.CharField(max_length=75L)
    class Meta:
        db_table = 'invitations_wpd'

class Lines(models.Model):
    linesid = models.IntegerField(primary_key=True)
    line = models.CharField(max_length=150L)
    description = models.CharField(max_length=5000L)
    class Meta:
        db_table = 'lines'

class Mailinglist(models.Model):
    mailinglistid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    name = models.CharField(max_length=60L, blank=True)
    email = models.CharField(max_length=100L, blank=True)
    address = models.CharField(max_length=200L, blank=True)
    city = models.CharField(max_length=50L, blank=True)
    state = models.CharField(max_length=10L, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    partyname = models.CharField(max_length=150L, blank=True)
    phone = models.CharField(max_length=15L, blank=True)
    rsvpceremony = models.IntegerField(null=True, blank=True)
    rsvpreception = models.IntegerField(null=True, blank=True)
    rsvpmeal = models.IntegerField(null=True, blank=True)
    active = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'mailinglist'

class Members(models.Model):
    membersid = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=150L, blank=True)
    websitename = models.CharField(max_length=50L, blank=True)
    password = models.CharField(max_length=50L, blank=True)
    gfirst_name = models.CharField(max_length=20L)
    glast_name = models.CharField(max_length=20L)
    bfirst_name = models.CharField(max_length=20L)
    blast_name = models.CharField(max_length=20L)
    zipcode = models.IntegerField(null=True)
    city = models.CharField(max_length=30L, blank=True)
    state = models.CharField(max_length=30L, blank=True)
    country = models.CharField(max_length=30L, blank=True)
    wedding_date = models.DateField()
    hero_image = models.FileField(upload_to='couples/', null=True)
    mainimage = models.CharField(max_length=150L, blank=True)
    mainimagew = models.IntegerField(null=True, blank=True)
    mainimageh = models.IntegerField(null=True, blank=True)
    path = models.CharField(max_length=200L, blank=True)
    active = models.IntegerField()
    photogallery = models.IntegerField(null=True, blank=True)
    template = models.CharField(max_length=10L)
    returnnum = models.IntegerField()
    stepprocess = models.IntegerField()
    viewable = models.IntegerField()
    newsletter = models.IntegerField()
    emailnum = models.IntegerField()
    emailopen = models.IntegerField()
    emailopen_date = models.DateField('Email Open', null=True, blank=True)
    class Meta:
        db_table = 'members'

class Newsletter(models.Model):
    newsletterid = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=150L)
    fname = models.CharField(max_length=20L)
    lname = models.CharField(max_length=20L)
    active = models.IntegerField()
    class Meta:
        db_table = 'newsletter'

class NewsletterInfo(models.Model):
    newsletter_infoid = models.IntegerField(primary_key=True)
    imagename = models.CharField(max_length=150L)
    caption = models.CharField(max_length=70L)
    body = models.CharField(max_length=5000L)
    date = models.DateField()
    name = models.CharField(max_length=70L)
    class Meta:
        db_table = 'newsletter_info'

class Ourstories(models.Model):
    ourstoriesid = models.IntegerField(primary_key=True)
    members = models.ForeignKey('Members')
    sex = models.CharField(max_length=6L)
    body = models.CharField(max_length=6000L, blank=True)
    date = models.DateField()
    active = models.IntegerField()
    class Meta:
        db_table = 'ourstories'

class PostComments(models.Model):
    post_comments_id = models.IntegerField(primary_key=True)
    posts_id = models.IntegerField()
    name = models.CharField(max_length=50L)
    comment = models.CharField(max_length=2000L)
    enabled = models.IntegerField()
    date_added = models.DateTimeField()
    class Meta:
        db_table = 'post_comments'

class Posts(models.Model):
    posts_id = models.IntegerField(primary_key=True)
    post_text = models.CharField(max_length=1000L)
    post_title = models.CharField(max_length=300L)
    enabled = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    class Meta:
        db_table = 'posts'

class PostsImages(models.Model):
    posts_images_id = models.IntegerField(primary_key=True)
    posts_id = models.IntegerField()
    imagename = models.CharField(max_length=128L)
    image_text = models.CharField(max_length=256L)
    orig_width = models.CharField(max_length=10L)
    orig_height = models.CharField(max_length=10L)
    date_added = models.DateTimeField()
    class Meta:
        db_table = 'posts_images'

class Quoterequest(models.Model):
    quoterequestid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40L)
    eventdate = models.CharField(max_length=30L)
    numpeople = models.CharField(max_length=10L)
    estbudget = models.CharField(max_length=10L)
    email = models.CharField(max_length=150L)
    question = models.CharField(max_length=600L)
    service_cat = models.CharField(max_length=50L)
    location = models.CharField(max_length=75L)
    email_verification = models.CharField(max_length=75L)
    date_time = models.DateTimeField()
    email_sent = models.IntegerField()
    class Meta:
        db_table = 'quoterequest'

class Quoteresponse(models.Model):
    quoteresponseid = models.IntegerField(primary_key=True)
    quoterequestid = models.IntegerField()
    vendorsid = models.IntegerField()
    response = models.CharField(max_length=1000L)
    datetime = models.DateTimeField()
    email_verification = models.CharField(max_length=75L)
    email_open = models.IntegerField()
    class Meta:
        db_table = 'quoteresponse'

class Registry(models.Model):
    registryid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    storename = models.CharField(max_length=50L)
    names = models.CharField(max_length=50L)
    phone = models.CharField(max_length=15L)
    address = models.CharField(max_length=150L)
    city = models.CharField(max_length=50L)
    state = models.CharField(max_length=20L)
    zipcode = models.CharField(max_length=5L)
    link = models.CharField(max_length=150L)
    active = models.IntegerField()
    class Meta:
        db_table = 'registry'

class Rsvp(models.Model):
    rsvpid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    name = models.CharField(max_length=40L, blank=True)
    mainquestion = models.CharField(max_length=100L, blank=True)
    maxattend = models.IntegerField(null=True, blank=True)
    meal = models.CharField(max_length=500L, blank=True)
    imagename = models.CharField(max_length=150L, blank=True)
    date = models.DateField(null=True, blank=True)
    active = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'rsvp'

class Rsvpguests(models.Model):
    rsvpguestsid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    name = models.CharField(max_length=60L)
    attending = models.IntegerField()
    meals = models.CharField(max_length=500L)
    specialreq = models.CharField(max_length=1000L)
    email = models.CharField(max_length=150L)
    class Meta:
        db_table = 'rsvpguests'

class Sitenav(models.Model):
    sitenavid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    welcome = models.CharField(max_length=45L)
    fromus = models.CharField(max_length=60L)
    ourstories = models.CharField(max_length=60L)
    weddingparty = models.CharField(max_length=60L)
    ourevents = models.CharField(max_length=60L)
    registry = models.CharField(max_length=60L)
    wishlist = models.CharField(max_length=60L)
    photos = models.CharField(max_length=60L)
    fromoutoftown = models.CharField(max_length=60L)
    rsvp = models.CharField(max_length=60L)
    guestbook = models.CharField(max_length=60L)
    extrainfo = models.CharField(max_length=60L)
    directions = models.CharField(max_length=60L)
    webmedia = models.CharField(max_length=60L)
    mailinglist = models.CharField(max_length=60L)
    family = models.CharField(max_length=60L)
    honeymoon = models.CharField(max_length=60L)
    contactus = models.CharField(max_length=60L)
    newsletter = models.CharField(max_length=60L)
    a_welcome = models.IntegerField()
    a_fromus = models.IntegerField()
    a_ourstories = models.IntegerField()
    a_weddingparty = models.IntegerField()
    a_ourevents = models.IntegerField()
    a_guestbook = models.IntegerField()
    a_registry = models.IntegerField()
    a_wishlist = models.IntegerField()
    a_photos = models.IntegerField()
    a_fromoutoftown = models.IntegerField()
    a_rsvp = models.IntegerField()
    a_newsletter = models.IntegerField()
    a_extrainfo = models.IntegerField()
    a_directions = models.IntegerField()
    a_webmedia = models.IntegerField()
    a_mailinglist = models.IntegerField()
    a_family = models.IntegerField()
    a_honeymoon = models.IntegerField()
    a_contactus = models.IntegerField()
    class Meta:
        db_table = 'sitenav'

class Tasklist(models.Model):
    tasklistid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200L)
    description = models.CharField(max_length=2000L, blank=True)
    position = models.IntegerField()
    category = models.CharField(max_length=45L)
    class Meta:
        db_table = 'tasklist'

class Vendors(models.Model):
    vendorsid = models.IntegerField(primary_key=True)
    vendorname = models.CharField(max_length=70L)
    contact_name = models.CharField(max_length=50L)
    service = models.CharField(max_length=40L, blank=True)
    address = models.CharField(max_length=100L, blank=True)
    city = models.CharField(max_length=40L, blank=True)
    state = models.CharField(max_length=25L, blank=True)
    zipcode = models.IntegerField()
    website = models.CharField(max_length=100L, blank=True)
    email = models.CharField(max_length=100L, blank=True)
    phone = models.CharField(max_length=17L, blank=True)
    fax = models.CharField(max_length=15L, blank=True)
    description = models.CharField(max_length=5000L, blank=True)
    addedby = models.CharField(max_length=15L)
    date = models.DateField()
    logo = models.CharField(max_length=200L, blank=True)
    package = models.IntegerField()
    portfolio1 = models.CharField(max_length=200L, blank=True)
    portfolio2 = models.CharField(max_length=200L, blank=True)
    portfolio3 = models.CharField(max_length=200L, blank=True)
    portfolio4 = models.CharField(max_length=200L, blank=True)
    portfolio5 = models.CharField(max_length=200L, blank=True)
    active = models.IntegerField()
    password = models.CharField(max_length=50L, blank=True)
    returnnum = models.IntegerField()
    featureimage = models.CharField(max_length=200L, blank=True)
    portfoliodesc1 = models.CharField(max_length=100L, blank=True)
    portfoliodesc2 = models.CharField(max_length=100L, blank=True)
    portfoliodesc3 = models.CharField(max_length=100L, blank=True)
    portfoliodesc4 = models.CharField(max_length=100L, blank=True)
    portfoliodesc5 = models.CharField(max_length=100L, blank=True)
    bannerimage = models.CharField(max_length=200L, blank=True)
    emailaction = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=5000L, blank=True)
    pagecount = models.IntegerField()
    sitecount = models.IntegerField(null=True, blank=True)
    websitecnt = models.IntegerField()
    trial_period = models.IntegerField()
    trial_start_date = models.DateField()
    offer_end_date = models.CharField(max_length=30L)
    newsletter = models.IntegerField()
    quote_option = models.IntegerField()
    emailnum = models.IntegerField()
    emailopen = models.IntegerField()
    class Meta:
        db_table = 'vendors'

class VendorsAddcontact(models.Model):
    vendors_addcontactid = models.IntegerField(primary_key=True)
    vendorsid = models.IntegerField()
    acctmgr = models.CharField(max_length=75L)
    rating = models.CharField(max_length=30L, blank=True)
    inbridalshow = models.CharField(max_length=30L, blank=True)
    monthlyadbudget = models.CharField(max_length=15L, blank=True)
    notamember = models.CharField(max_length=30L, blank=True)
    class Meta:
        db_table = 'vendors_addcontact'

class VendorsContacts(models.Model):
    vendors_contactsid = models.IntegerField(primary_key=True)
    vendorsid = models.IntegerField()
    prefix = models.CharField(max_length=5L, blank=True)
    firstname = models.CharField(max_length=45L, blank=True)
    lastname = models.CharField(max_length=45L, blank=True)
    title = models.CharField(max_length=45L, blank=True)
    mobile = models.CharField(max_length=20L, blank=True)
    email = models.CharField(max_length=150L, blank=True)
    description = models.CharField(max_length=500L, blank=True)
    class Meta:
        db_table = 'vendors_contacts'

class VendorsSitecount(models.Model):
    vendors_sitecount = models.IntegerField(primary_key=True)
    vendorid = models.IntegerField()
    zipcode = models.CharField(max_length=10L)
    referrer = models.CharField(max_length=200L)
    userip = models.CharField(max_length=30L)
    user_agent = models.CharField(max_length=200L)
    linktype = models.CharField(max_length=15L)
    page = models.CharField(max_length=20L)
    datetime = models.DateTimeField()
    class Meta:
        db_table = 'vendors_sitecount'

class Weddingparty(models.Model):
    weddingpartyid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    body = models.CharField(max_length=5000L)
    title = models.CharField(max_length=40L)
    name = models.CharField(max_length=40L)
    imagename = models.CharField(max_length=200L)
    type = models.CharField(max_length=10L)
    active = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = 'weddingparty'

class Welcome(models.Model):
    welcomeid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    title = models.CharField(max_length=50L, blank=True)
    body = models.CharField(max_length=3000L, blank=True)
    mainimage = models.CharField(max_length=200L, blank=True)
    date = models.DateField(null=True, blank=True)
    last_updated = models.DateTimeField()
    active = models.IntegerField()
    class Meta:
        db_table = 'welcome'

class Wishlist(models.Model):
    wishlistid = models.IntegerField(primary_key=True)
    membersid = models.ForeignKey('Members')
    wishname = models.CharField(max_length=60L)
    names = models.CharField(max_length=60L)
    phone = models.CharField(max_length=15L)
    address = models.CharField(max_length=150L)
    city = models.CharField(max_length=60L)
    state = models.CharField(max_length=30L)
    zipcode = models.CharField(max_length=12L)
    link = models.CharField(max_length=150L)
    active = models.IntegerField()
    class Meta:
        db_table = 'wishlist'

class Zipcode(models.Model):
    zipcode = models.IntegerField()
    stateabbr = models.CharField(max_length=10L)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=28L)
    state = models.CharField(max_length=30L)
    class Meta:
        db_table = 'zipcode'

