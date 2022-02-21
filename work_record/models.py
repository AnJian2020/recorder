from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PolicyDocumentModel(models.Model):
    id = models.CharField(verbose_name='id', max_length=32, primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=256)
    content = models.TextField(verbose_name='正文', blank=True, null=True, default='正文点击链接查看')
    link = models.CharField(verbose_name="链接", max_length=512)
    publish_time = models.DateField(verbose_name="发表时间")
    units_concerned = models.CharField(verbose_name="有关单位", max_length=512)
    submit_time = models.DateTimeField(verbose_name='提交时间', default=timezone.now)
    edit_time = models.DateTimeField(verbose_name='最后编辑时间', default=timezone.now)
    submit_user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='提交人员')
    is_alter = models.BooleanField(verbose_name='锁定', default=True)

    def __str__(self):
        return "id: %s title: %s" % (self.id, self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.submit_time = timezone.now()
            self.id = 'PD' + self.submit_time.year.__str__() + self.submit_time.month.__str__() + \
                      self.submit_time.day.__str__() + self.submit_time.hour.__str__() + self.submit_time.minute.__str__() + \
                      self.submit_time.second.__str__()
        self.edit_time = timezone.now()
        return super(PolicyDocumentModel, self).save(*args, **kwargs)

    class Meta:
        db_table = 'policy_document_table'
        verbose_name = "政策文件表"
        verbose_name_plural = '政策文件表'


class IndustryDevelopmentModel(models.Model):
    id = models.CharField(verbose_name='id', max_length=32, primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=256)

    class IndustryCategory(models.TextChoices):
        FARMING_FORESTRY_ANIMAL_HUSBANDRY_FISHERY = 'FFAHF', '农、林、牧、渔业'
        MINING = 'MINING', '采矿业'
        MANUFACTURING_INDUSTRY = 'MANUFACTURING_INDUSTRY', '制造业'
        ELECTRICITY_HEAT_GAS_WATER = "ELECTRICITY_HEAT_GAS_WATER", '电力、热力、燃气及水生产和供应业'
        CONSTRUCTION_INDUSTRY = 'CONSTRUCTION_INDUSTRY', '建筑业'
        WHOLESALE_RETAIL = 'WHOLESALE_RETAIL', '批发和零售业'
        TRANSPORTATION_WAREHOUSING_POSTAL_SERVICES = 'TRANSPORTATION_WAREHOUSING_POSTAL_SERVICES', '交通运输、仓储和邮政业'
        ACCOMMODATION_CATERING = 'ACCOMMODATION_CATERING', '住宿和餐饮业'
        INFORMATION_TRANSMISSION_SOFTWARE_INFORMATION_TECHNOLOGY_SERVICES = 'IT', '信息传输、软件和信息技术服务业'
        FINANCIAL_SECTOR = 'FINANCIAL_SECTOR', '金融业'
        REAL_ESTATE_INDUSTRY = 'REAL_ESTATE_INDUSTRY', '房地产业'
        LEASING_BUSINESS_SERVICES = 'LEASING_BUSINESS_SERVICES', '租赁和商务服务业'
        SCIENTIFIC_RESEARCH_TECHNOLOGY_SERVICES = 'SCIENTIFIC_RESEARCH_TECHNOLOGY_SERVICES', '科学研究和技术服务业'
        WATER_CONSERVANCY_ENVIRONMENT_PUBLIC_FACILITIES_MANAGEMENT = 'WCEPFM', '水利、环境和公共设施管理业'
        RESIDENTIAL_SERVICES_REPAIRS_OTHER_SERVICES = 'RSROS', '居民服务、修理和其他服务业'
        EDUCATION = 'EDUCATION', '教育'
        HEALTH_SOCIAL_WORK = 'HEALTH_SOCIAL_WORK', '卫生和社会工作'
        CULTURE_SPORTS_ENTERTAINMENT = 'CULTURE_SPORTS_ENTERTAINMENT', '文化、体育和娱乐业'
        PUBLIC_ADMINISTRATION_SOCIAL_SECURITY_SOCIAL_ORGANIZATION = 'PASSSO', '公共管理、社会保障和社会组织'
        INTERNATIONAL_ORGANIZATION = 'INTERNATIONAL_ORGANIZATION', '国际组织'

    industry_category = models.CharField(verbose_name='行业类型', max_length=256, choices=IndustryCategory.choices,
                                         default=IndustryCategory.INFORMATION_TRANSMISSION_SOFTWARE_INFORMATION_TECHNOLOGY_SERVICES)
    file_link = models.FileField(verbose_name='文件链接', upload_to='industry_development/%Y/%m/%d')
    brief_introduction = models.CharField(verbose_name="简介", max_length=512)
    units_concerned = models.CharField(verbose_name="有关单位", max_length=512)
    publish_time = models.DateField(verbose_name="发表时间", default=timezone.now)
    submit_time = models.DateTimeField(verbose_name='提交时间', default=timezone.now)
    edit_time = models.DateTimeField(verbose_name="最后编辑时间", default=timezone.now)
    submit_user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="提交人员")

    def __str__(self):
        return "id: %s title: %s" % (self.id, self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.submit_time = timezone.now()
            self.id = 'ID' + self.submit_time.year.__str__() + self.submit_time.month.__str__() + \
                      self.submit_time.day.__str__() + self.submit_time.hour.__str__() + self.submit_time.minute.__str__() + \
                      self.submit_time.second.__str__()
        self.edit_time = timezone.now()
        return super(IndustryDevelopmentModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "行业发展报告"
        verbose_name_plural = "行业发展报告"
        db_table = "industry_development_table"
