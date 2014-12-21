# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class WpCommentmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'wp_commentmeta'

class WpComments(models.Model):
    comment_id = models.BigIntegerField(primary_key=True, db_column='comment_ID') # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID') # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100L)
    comment_author_url = models.CharField(max_length=200L)
    comment_author_ip = models.CharField(max_length=100L, db_column='comment_author_IP') # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20L)
    comment_agent = models.CharField(max_length=255L)
    comment_type = models.CharField(max_length=20L)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()
    class Meta:
        db_table = 'wp_comments'

class WpFrontendBuilderOptions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    value = models.TextField()
    class Meta:
        db_table = 'wp_frontend_builder_options'

class WpFrontendBuilderPages(models.Model):
    id = models.IntegerField(primary_key=True)
    switch = models.TextField()
    layout = models.TextField()
    items = models.TextField()
    class Meta:
        db_table = 'wp_frontend_builder_pages'

class WpLinks(models.Model):
    link_id = models.BigIntegerField(primary_key=True)
    link_url = models.CharField(max_length=255L)
    link_name = models.CharField(max_length=255L)
    link_image = models.CharField(max_length=255L)
    link_target = models.CharField(max_length=25L)
    link_description = models.CharField(max_length=255L)
    link_visible = models.CharField(max_length=20L)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255L)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255L)
    class Meta:
        db_table = 'wp_links'

class WpOptions(models.Model):
    option_id = models.BigIntegerField(primary_key=True)
    option_name = models.CharField(max_length=64L, unique=True)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20L)
    class Meta:
        db_table = 'wp_options'

class WpPostmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'wp_postmeta'

class WpPosts(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20L)
    comment_status = models.CharField(max_length=20L)
    ping_status = models.CharField(max_length=20L)
    post_password = models.CharField(max_length=20L)
    post_name = models.CharField(max_length=200L)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255L)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20L)
    post_mime_type = models.CharField(max_length=100L)
    comment_count = models.BigIntegerField()
    class Meta:
        db_table = 'wp_posts'

class WpRevsliderCss(models.Model):
    id = models.IntegerField(primary_key=True)
    handle = models.TextField()
    settings = models.TextField(blank=True)
    hover = models.TextField(blank=True)
    params = models.TextField()
    class Meta:
        db_table = 'wp_revslider_css'

class WpRevsliderLayerAnimations(models.Model):
    id = models.IntegerField(primary_key=True)
    handle = models.TextField()
    params = models.TextField()
    class Meta:
        db_table = 'wp_revslider_layer_animations'

class WpRevsliderSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    general = models.TextField()
    params = models.TextField()
    class Meta:
        db_table = 'wp_revslider_settings'

class WpRevsliderSliders(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    alias = models.TextField(blank=True)
    params = models.TextField()
    class Meta:
        db_table = 'wp_revslider_sliders'

class WpRevsliderSlides(models.Model):
    id = models.IntegerField(primary_key=True)
    slider_id = models.IntegerField()
    slide_order = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    class Meta:
        db_table = 'wp_revslider_slides'

class WpSendpressListSubscribers(models.Model):
    id = models.IntegerField(primary_key=True)
    listid = models.IntegerField(null=True, db_column='listID', blank=True) # Field name made lowercase.
    subscriberid = models.IntegerField(null=True, db_column='subscriberID', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, blank=True)
    updated = models.DateTimeField()
    class Meta:
        db_table = 'wp_sendpress_list_subscribers'

class WpSendpressQueue(models.Model):
    id = models.IntegerField(primary_key=True)
    subscriberid = models.IntegerField(null=True, db_column='subscriberID', blank=True) # Field name made lowercase.
    listid = models.IntegerField(null=True, db_column='listID', blank=True) # Field name made lowercase.
    from_name = models.CharField(max_length=64L, blank=True)
    from_email = models.CharField(max_length=128L)
    to_email = models.CharField(max_length=128L)
    subject = models.CharField(max_length=255L)
    messageid = models.CharField(max_length=400L, db_column='messageID') # Field name made lowercase.
    emailid = models.IntegerField(db_column='emailID') # Field name made lowercase.
    max_attempts = models.IntegerField()
    attempts = models.IntegerField()
    success = models.IntegerField()
    date_published = models.DateTimeField()
    inprocess = models.IntegerField(null=True, blank=True)
    last_attempt = models.DateTimeField()
    date_sent = models.DateTimeField()
    class Meta:
        db_table = 'wp_sendpress_queue'

class WpSendpressReportUrl(models.Model):
    urlid = models.IntegerField(primary_key=True, db_column='urlID') # Field name made lowercase.
    url = models.CharField(max_length=2000L, blank=True)
    reportid = models.IntegerField(null=True, db_column='reportID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'wp_sendpress_report_url'

class WpSendpressSubscribers(models.Model):
    subscriberid = models.BigIntegerField(primary_key=True, db_column='subscriberID') # Field name made lowercase.
    email = models.CharField(max_length=100L, unique=True)
    join_date = models.DateTimeField()
    status = models.IntegerField()
    registered = models.DateTimeField()
    registered_ip = models.CharField(max_length=20L)
    identity_key = models.CharField(max_length=60L, unique=True)
    bounced = models.IntegerField()
    firstname = models.CharField(max_length=250L)
    lastname = models.CharField(max_length=250L)
    wp_user_id = models.BigIntegerField(unique=True, null=True, blank=True)
    class Meta:
        db_table = 'wp_sendpress_subscribers'

class WpSendpressSubscribersEvent(models.Model):
    eventid = models.IntegerField(primary_key=True, db_column='eventID') # Field name made lowercase.
    subscriberid = models.IntegerField(db_column='subscriberID') # Field name made lowercase.
    reportid = models.IntegerField(null=True, db_column='reportID', blank=True) # Field name made lowercase.
    urlid = models.IntegerField(null=True, db_column='urlID', blank=True) # Field name made lowercase.
    listid = models.IntegerField(null=True, db_column='listID', blank=True) # Field name made lowercase.
    eventdate = models.DateTimeField()
    ip = models.CharField(max_length=400L, blank=True)
    devicetype = models.CharField(max_length=50L, blank=True)
    device = models.CharField(max_length=50L, blank=True)
    type = models.CharField(max_length=50L, blank=True)
    class Meta:
        db_table = 'wp_sendpress_subscribers_event'

class WpSendpressSubscribersMeta(models.Model):
    smeta_id = models.BigIntegerField(primary_key=True)
    subscriberid = models.BigIntegerField(db_column='subscriberID') # Field name made lowercase.
    listid = models.BigIntegerField(null=True, db_column='listID', blank=True) # Field name made lowercase.
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'wp_sendpress_subscribers_meta'

class WpSendpressSubscribersStatus(models.Model):
    statusid = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'wp_sendpress_subscribers_status'

class WpTermRelationships(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()
    class Meta:
        db_table = 'wp_term_relationships'

class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigIntegerField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32L)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()
    class Meta:
        db_table = 'wp_term_taxonomy'

class WpTerms(models.Model):
    term_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200L)
    slug = models.CharField(max_length=200L, unique=True)
    term_group = models.BigIntegerField()
    class Meta:
        db_table = 'wp_terms'

class WpUsermeta(models.Model):
    umeta_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'wp_usermeta'

class WpUsers(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    user_login = models.CharField(max_length=60L)
    user_pass = models.CharField(max_length=64L)
    user_nicename = models.CharField(max_length=50L)
    user_email = models.CharField(max_length=100L)
    user_url = models.CharField(max_length=100L)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=60L)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250L)
    class Meta:
        db_table = 'wp_users'

class WpWoocommerceAttributeTaxonomies(models.Model):
    attribute_id = models.BigIntegerField(primary_key=True)
    attribute_name = models.CharField(max_length=200L)
    attribute_label = models.TextField(blank=True)
    attribute_type = models.CharField(max_length=200L)
    attribute_orderby = models.CharField(max_length=200L)
    class Meta:
        db_table = 'wp_woocommerce_attribute_taxonomies'

class WpWoocommerceDownloadableProductPermissions(models.Model):
    download_id = models.CharField(max_length=32L)
    product_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    order_key = models.CharField(max_length=200L)
    user_email = models.CharField(max_length=200L)
    user_id = models.BigIntegerField(null=True, blank=True)
    downloads_remaining = models.CharField(max_length=9L, blank=True)
    access_granted = models.DateTimeField()
    access_expires = models.DateTimeField(null=True, blank=True)
    download_count = models.BigIntegerField()
    class Meta:
        db_table = 'wp_woocommerce_downloadable_product_permissions'

class WpWoocommerceOrderItemmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    order_item_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'wp_woocommerce_order_itemmeta'

class WpWoocommerceOrderItems(models.Model):
    order_item_id = models.BigIntegerField(primary_key=True)
    order_item_name = models.TextField()
    order_item_type = models.CharField(max_length=200L)
    order_id = models.BigIntegerField()
    class Meta:
        db_table = 'wp_woocommerce_order_items'

class WpWoocommerceTaxRateLocations(models.Model):
    location_id = models.BigIntegerField(primary_key=True)
    location_code = models.CharField(max_length=255L)
    tax_rate_id = models.BigIntegerField()
    location_type = models.CharField(max_length=40L)
    class Meta:
        db_table = 'wp_woocommerce_tax_rate_locations'

class WpWoocommerceTaxRates(models.Model):
    tax_rate_id = models.BigIntegerField(primary_key=True)
    tax_rate_country = models.CharField(max_length=200L)
    tax_rate_state = models.CharField(max_length=200L)
    tax_rate = models.CharField(max_length=200L)
    tax_rate_name = models.CharField(max_length=200L)
    tax_rate_priority = models.BigIntegerField()
    tax_rate_compound = models.IntegerField()
    tax_rate_shipping = models.IntegerField()
    tax_rate_order = models.BigIntegerField()
    tax_rate_class = models.CharField(max_length=200L)
    class Meta:
        db_table = 'wp_woocommerce_tax_rates'

class WpWoocommerceTermmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    woocommerce_term_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'wp_woocommerce_termmeta'

class WpYopPollAnswermeta(models.Model):
    meta_id = models.IntegerField(primary_key=True)
    yop_poll_answer_id = models.IntegerField()
    meta_key = models.CharField(max_length=255L)
    meta_value = models.TextField()
    class Meta:
        db_table = 'wp_yop_poll_answermeta'

class WpYopPollAnswers(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    answer = models.CharField(max_length=255L)
    type = models.CharField(max_length=7L)
    votes = models.IntegerField()
    status = models.CharField(max_length=255L)
    class Meta:
        db_table = 'wp_yop_poll_answers'

class WpYopPollBans(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    type = models.CharField(max_length=255L)
    value = models.CharField(max_length=255L)
    class Meta:
        db_table = 'wp_yop_poll_bans'

class WpYopPollCustomFields(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    custom_field = models.CharField(max_length=255L)
    required = models.CharField(max_length=3L)
    status = models.CharField(max_length=255L)
    class Meta:
        db_table = 'wp_yop_poll_custom_fields'

class WpYopPollFacebookUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    fb_id = models.CharField(max_length=255L)
    name = models.CharField(max_length=255L)
    first_name = models.CharField(max_length=255L)
    last_name = models.CharField(max_length=255L)
    username = models.CharField(max_length=255L)
    email = models.CharField(max_length=255L)
    gender = models.CharField(max_length=255L)
    date_added = models.DateTimeField()
    class Meta:
        db_table = 'wp_yop_poll_facebook_users'

class WpYopPollLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    vote_id = models.CharField(max_length=255L)
    answer_id = models.IntegerField()
    ip = models.CharField(max_length=100L)
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=9L)
    http_referer = models.CharField(max_length=255L)
    tr_id = models.CharField(max_length=255L)
    other_answer_value = models.TextField()
    host = models.CharField(max_length=200L)
    vote_date = models.DateTimeField()
    class Meta:
        db_table = 'wp_yop_poll_logs'

class WpYopPollTemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    template_author = models.BigIntegerField()
    name = models.CharField(max_length=255L)
    before_vote_template = models.TextField()
    after_vote_template = models.TextField()
    before_start_date_template = models.TextField()
    after_end_date_template = models.TextField()
    css = models.TextField()
    js = models.TextField()
    status = models.CharField(max_length=255L)
    last_modified = models.DateTimeField()
    date_added = models.DateTimeField()
    class Meta:
        db_table = 'wp_yop_poll_templates'

class WpYopPollVoters(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=9L)
    class Meta:
        db_table = 'wp_yop_poll_voters'

class WpYopPollVotesCustomFields(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    vote_id = models.CharField(max_length=255L)
    custom_field_id = models.IntegerField()
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=9L)
    custom_field_value = models.TextField()
    tr_id = models.CharField(max_length=255L)
    vote_date = models.DateTimeField()
    class Meta:
        db_table = 'wp_yop_poll_votes_custom_fields'

class WpYopPollmeta(models.Model):
    meta_id = models.IntegerField(primary_key=True)
    yop_poll_id = models.IntegerField()
    meta_key = models.CharField(max_length=255L)
    meta_value = models.TextField()
    class Meta:
        db_table = 'wp_yop_pollmeta'

class WpYopPolls(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_author = models.BigIntegerField()
    name = models.CharField(max_length=255L)
    question = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_votes = models.IntegerField()
    total_answers = models.IntegerField()
    status = models.CharField(max_length=255L)
    last_modified = models.DateTimeField()
    date_added = models.DateTimeField()
    show_in_archive = models.CharField(max_length=3L)
    archive_order = models.IntegerField()
    class Meta:
        db_table = 'wp_yop_polls'

