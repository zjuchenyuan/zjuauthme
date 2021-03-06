CACHE = {}
CACHE["xiaoqu"] = ['之江校区', '玉泉校区', '紫金港校区', '舟山校区', '西溪校区']
CACHE["xiaoqu_louyu"] = {
            '紫金港校区': ['东一C', '农生环组团A座', '农生环组团B座', '农生环组团C座', '农生环组团E座', ' 医学院科研辅楼', '医学院综合楼', '南华园', '图书信息中心C楼', '校友楼', '生命科学学院大楼', '纳米楼', '蒙民伟楼'], 
            '西溪校区': ['逸夫科教馆'], 
            '玉泉校区': ['周亦卿科技大楼', '永谦学生活动中心', '第七教学大楼', '行政楼', '邵逸夫科学馆'], 
            '之江校区': ['李作权学生活动中心'], 
            '舟山校区': ['图书馆', '智海楼', '海工楼', '海科楼', '行政楼']
}
CACHE["louyu"] = ['东一C', '校友楼', '生命科学学院大楼', '逸夫科教馆', '农生环组团E座', '图书信息中心C楼', '智海楼', '医学院综合楼', '蒙民伟楼', '邵逸夫科学馆', '纳米楼', '周亦卿科技大楼', '李作权学生活动中心', '海工楼', '永谦学生活动中心', '行政楼', '第七教学大楼', '农生环组团B座', '农生环组团C座', '南华园', '医学院科研辅楼', '图书馆', '农生环组团A座', '海科楼']
CACHE["louyu_ziyuan"] = {'东一C': [('286', '临水报告厅')],
 '农生环组团A座': [('296', 'A110报告厅'),
             ('297', 'A214贵宾室'),
             ('298', 'A216会议室'),
             ('299', 'A218会议室')],
 '农生环组团B座': [('300', 'B110会议室'),
             ('301', 'B112报告厅'),
             ('302', 'B125会议室'),
             ('303', 'B126会议室'),
             ('304', 'B127会议室')],
 '农生环组团C座': [('305', 'C102邦华厅'), ('306', 'C1212贵宾室'), ('314', 'C316报告厅')],
 '农生环组团E座': [('307', 'E122报告厅'),
             ('308', 'E222报告厅'),
             ('309', 'E248会议室'),
             ('310', 'E250会议室'),
             ('311', 'E316报告厅'),
             ('312', 'E412报告厅'),
             ('313', 'E524报告厅')],
 '医学院科研辅楼': [('293', '报告厅')],
 '医学院综合楼': [('287', '205会议室'),
            ('290', '701会议室'),
            ('446', '705会议室'),
            ('291', '712会议室'),
            ('292', '713会议室'),
            ('447', '715会议室'),
            ('448', '716会议室')],
 '南华园': [('279', '1号楼'), ('280', '2号楼')],
 '周亦卿科技大楼': [('267', '一楼报告厅')],
 '图书信息中心C楼': [('263', '17楼贵宾室')],
 '图书馆': [('440', '402学习讨论室'),
         ('423', '403学习讨论室'),
         ('424', '404学术交流室'),
         ('441', '502学习讨论室'),
         ('425', '503学术交流室'),
         ('444', '二楼大厅视频空间'),
         ('445', '二楼悦空间'),
         ('426', '学生中心700人报告厅')],
 '智海楼': [('428', '智海楼145')],
 '李作权学生活动中心': [('278', '多功能厅'),
               ('275', '报告厅'),
               ('276', '第一会议室'),
               ('277', '第二会议室')],
 '校友楼': [('360', '玉泉厅'), ('367', '紫金港厅'), ('366', '舟山厅-贵宾室'), ('359', '西溪厅')],
 '永谦学生活动中心': [('325', 'A102会议室'),
              ('326', 'A103会议室'),
              ('327', 'A104会议室'),
              ('328', 'A105会议室'),
              ('320', 'A110会议室'),
              ('329', 'A201会议室'),
              ('330', 'A202会议室'),
              ('331', 'A203会议室'),
              ('332', 'A204会议室'),
              ('333', 'A205会议室'),
              ('321', 'A210会议室'),
              ('334', 'A301会议室'),
              ('335', 'A302会议室'),
              ('336', 'A303会议室'),
              ('337', 'A304会议室'),
              ('338', 'A305会议室'),
              ('339', 'A306会议室'),
              ('340', 'A307会议室 '),
              ('322', 'A座二楼会议室'),
              ('323', 'B011会议室'),
              ('324', 'B012会议室'),
              ('316', 'B座一楼报告厅'),
              ('319', 'B座三楼多功能厅'),
              ('317', 'B座二楼报告厅'),
              ('318', 'B座二楼排练厅'),
              ('315', '小剧场')],
 '海工楼': [('410', '海工楼327'), ('411', '海工楼414')],
 '海科楼': [('442', '海科楼301'), ('412', '海科楼342-344'), ('413', '海科楼416-418')],
 '生命科学学院大楼': [('295', '123会议室'), ('294', '245报告厅')],
 '第七教学大楼': [('268', '教学影视厅')],
 '纳米楼': [('355', '301贵宾室'),
         ('407', '307会客室'),
         ('368', '310会议室'),
         ('408', '407会议室'),
         ('357', '412会议室'),
         ('406', '414会客室'),
         ('399', '512会议室'),
         ('356', '514会议室')],
 '蒙民伟楼': [('282', '138报告厅'),
          ('283', '139报告厅'),
          ('284', '223报告厅'),
          ('285', '225报告厅')],
 '行政楼': [('266', '第三会议室'),
         ('265', '第二会客室'),
         ('414', '行政楼101'),
         ('415', '行政楼126'),
         ('416', '行政楼201'),
         ('417', '行政楼230'),
         ('418', '行政楼304'),
         ('419', '行政楼330'),
         ('420', '行政楼402'),
         ('421', '行政楼428（贵宾室）')],
 '逸夫科教馆': [('271', '113会议室（已停用）'), ('269', '207报告厅'), ('270', '301会议室')],
 '邵逸夫科学馆': [('354', '117会议室'),
            ('344', '201会议室'),
            ('345', '203会议室'),
            ('346', '204会议室'),
            ('347', '205会议室'),
            ('348', '206会议室'),
            ('349', '209会议室'),
            ('352', '211-212室'),
            ('350', '211会议室'),
            ('351', '212会议室'),
            ('353', '贵宾室')]
}
CACHE["ziyuan"]=[('426', '学生中心700人报告厅'), ('295', '123会议室'), ('353', '贵宾室'), ('350', '211会议室'), ('322', 'A座二楼会议室'), ('305', 'C102邦华厅'), ('368', '310会议室'), ('332', 'A204会议室'), ('297', 'A214贵宾室'), ('424', '404学术交流室'), ('320', 'A110会议室'), ('348', '206会议室'), ('406', '414会客室'), ('333', 'A205会议室'), ('280', '2号楼'), ('312', 'E412报告厅'), ('329', 'A201会议室'), ('283', '139报告厅'), ('423', '403学习讨论室'), ('419', '行政楼330'), ('303', 'B126会议室'), ('294', '245报告厅'), ('356', '514会议室'), ('351', '212会议室'), ('323', 'B011会议室'), ('263', '17楼贵宾室'), ('399', '512会议室'), ('306', 'C1212贵宾室'), ('417', '行政楼230'), ('291', '712会议室'), ('311', 'E316报告厅'), ('345', '203会议室'), ('408', '407会议室'), ('448', '716会议室'), ('314', 'C316报告厅'), ('412', '海科楼342-344'), ('325', 'A102会议室'), ('267', '一楼报告厅'), ('324', 'B012会议室'), ('316', 'B座一楼报告厅'), ('309', 'E248会议室'), ('445', '二楼悦空间'), ('347', '205会议室'), ('442', '海科楼301'), ('335', 'A302会议室'), ('319', 'B座三楼多功能厅'), ('418', '行政楼304'), ('349', '209会议室'), ('334', 'A301会议室'), ('336', 'A303会议室'), ('416', '行政楼201'), ('276', '第一会议室'), ('317', 'B座二楼报告厅'), ('428', '智海楼145'), ('302', 'B125会议室'), ('296', 'A110报告厅'), ('300', 'B110会议室'), ('277', '第二会议室'), ('298', 'A216会议室'), ('268', '教学影视厅'), ('421', '行政楼428（贵宾室）'), ('367', '紫金港厅'), ('304', 'B127会议室'), ('301', 'B112报告厅'), ('366', '舟山厅-贵宾室'), ('327', 'A104会议室'), ('265', '第二会客室'), ('359', '西溪厅'), ('287', '205会议室'), ('270', '301会议室'), ('446', '705会议室'), ('444', '二楼大厅视频空间'), ('410', '海工楼327'), ('278', '多功能厅'), ('292', '713会议室'), ('338', 'A305会议室'), ('447', '715会议室'), ('285', '225报告厅'), ('293', '报告厅'), ('321', 'A210会议室'), ('407', '307会客室'), ('308', 'E222报告厅'), ('352', '211-212室'), ('282', '138报告厅'), ('354', '117会议室'), ('266', '第三会议室'), ('340', 'A307会议室 '), ('411', '海工楼414'), ('360', '玉泉厅'), ('440', '402学习讨论室'), ('414', '行政楼101'), ('331', 'A203会议室'), ('339', 'A306会议室'), ('275', '报告厅'), ('413', '海科楼416-418'), ('284', '223报告厅'), ('328', 'A105会议室'), ('271', '113会议室（已停用）'), ('346', '204会议室'), ('307', 'E122报告厅'), ('318', 'B座二楼排练厅'), ('269', '207报告厅'), ('415', '行政楼126'), ('310', 'E250会议室'), ('330', 'A202会议室'), ('290', '701会议室'), ('357', '412会议室'), ('286', '临水报告厅'), ('279', '1号楼'), ('315', '小剧场'), ('326', 'A103会议室'), ('337', 'A304会议室'), ('313', 'E524报告厅'), ('344', '201会议室'), ('420', '行政楼402'), ('441', '502学习讨论室'), ('425', '503学术交流室'), ('355', '301贵宾室'), ('299', 'A218会议室')]