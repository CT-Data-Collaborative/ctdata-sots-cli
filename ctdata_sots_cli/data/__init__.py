from collections import OrderedDict

tx_codes = [OrderedDict([('cd_trans_type', 'ACAS'),
                         ('label', 'AGENT ADDRESS CHANGE FOR STOCK CORPORATIONS (DOMESTIC, BENEFIT & FOREIGN)'),
                         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'),
                         ('benefit', 'TRUE'), ('company_type', 'CORP')]), OrderedDict(
    [('cd_trans_type', 'ACS'), ('label', 'AGENT CHANGE FOR STOCK CORPORATIONS (DOMESTIC,BENEFIT & FOREIGN)'),
     ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'TRUE'),
     ('company_type', 'CORP')]), OrderedDict(
    [('cd_trans_type', 'CINC'), ('label', 'INTERIM NOTICE FOR CORPORATIONS (DOMESTIC, BENEFIT & FOREIGN)'),
     ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'TRUE'),
     ('company_type', 'CORP')]), OrderedDict(
    [('cd_trans_type', 'COB'), ('label', 'ORGANIZATION AND FIRST REPORT FOR BENEFIT CORPORATION'),
     ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'TRUE'),
     ('company_type', 'BEN')]), OrderedDict(
    [('cd_trans_type', 'CRS'), ('label', 'ANNUAL REPORT FOR STOCK CORPORATION (DOMESTIC & BENEFIT)'),
     ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'TRUE'),
     ('company_type', 'CORP')]), OrderedDict(
    [('cd_trans_type', 'ACAN'), ('label', 'AGENT ADDRESS CHANGE FOR NON-STOCK CORPORATIONS (DOMESTIC & FOREIGN)'),
     ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
     ('company_type', 'CORP')]), OrderedDict(
    [('cd_trans_type', 'ACN'), ('label', 'AGENT CHANGE FOR NON-STOCK CORPORATIONS (DOMESTIC & FOREIGN)'),
     ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
     ('company_type', 'CORP')]), OrderedDict(
    [('cd_trans_type', 'ASRN'), ('label', 'RESIGNATION OF AGENT FOR NON-STOCK CORPORATIONS (DOMESTIC & FOREIGN)'),
     ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
     ('company_type', 'CORP')]), OrderedDict(
    [('cd_trans_type', 'ASRS'), ('label', 'RESIGNATION OF AGENT FOR STOCK CORPORATIONS (DOMESTIC & FOREIGN)'),
     ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
     ('company_type', 'CORP')]), OrderedDict(
    [('cd_trans_type', 'BAN'), ('label', 'BUSINESS AMENDMENT FOR BANK (NON-STOCK)'), ('stock', 'FALSE'),
     ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'BANK')]),
            OrderedDict(
                [('cd_trans_type', 'BAS'), ('label', 'BUSINESS AMENDMENT FOR BANK (STOCK)'), ('stock', 'TRUE'),
                 ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
                 ('company_type', 'BANK')]), OrderedDict(
        [('cd_trans_type', 'BCORP'), ('label', 'BUSINESS FORMATION FOR BENEFIT CORPORATION'), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'BEN')]), OrderedDict(
        [('cd_trans_type', 'BN'), ('label', 'BUSINESS FORMATION FOR DOMESTIC BANK (NON-STOCK)'), ('stock', 'FALSE'),
         ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'BANK')]),
            OrderedDict([('cd_trans_type', 'BS'), ('label', 'BUSINESS FORMATION FOR DOMESTIC BANK (STOCK)'),
                         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', 'BANK')]), OrderedDict(
        [('cd_trans_type', 'CAFN'), ('label', 'BUSINESS AMENDMENT FOR NON-STOCK CORPORATION (FOREIGN) '),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CAFS'), ('label', 'BUSINESS AMENDMENT FOR STOCK CORPORATION (FOREIGN) '),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CAN'), ('label', 'BUSINESS AMENDMENT FOR NON-STOCK CORPORATION (DOMESTIC) '),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CAS'), ('label', 'BUSINESS AMENDMENT FOR STOCK CORPORATION (DOMESTIC) '),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CASCN'), ('label', 'BUSINESS AMENDMENT FOR NON-STOCK CORPORATION (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CASCS'), ('label', 'BUSINESS AMENDMENT FOR STOCK CORPORATION (FOREIGN) '),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CCORMS'), (
        'label', 'CERTIFICATE OF CORRECTION IN MERGER FOR STOCK CORPORATIONS (DOMESTIC & FOREIGN)'), ('stock', 'TRUE'),
                                          ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'),
                                          ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CCORN'),
         ('label', 'CERTIFICATE OF CORRECTION FOR NON-STOCK CORPORATIONS (DOMESTIC & FOREIGN)'), ('stock', 'FALSE'),
         ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'), ('company_type', 'CORP')]),
            OrderedDict([('cd_trans_type', 'CDRN'), ('label', 'DISSOLUTION FOR NON-STOCK CORPORATION (DOMESTIC)'),
                         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CDRNNR'), ('label', 'DISSOLUTION FOR RELIGIOUS (NON-STOCK)'), ('stock', 'FALSE'),
         ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'REL')]),
            OrderedDict([('cd_trans_type', 'CDRS'), ('label', 'DISSOLUTION FOR STOCK CORPORATION (DOMESTIC)'),
                         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CDRSNR'), ('label', 'DISSOLUTION FOR RELIGIOUS (STOCK)'), ('stock', 'TRUE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'REL')]), OrderedDict(
        [('cd_trans_type', 'CFAN'), ('label', 'BUSINESS FORMATION FOR NON-STOCK CORPORATION (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CFAS'), ('label', 'BUSINESS FORMATION FOR STOCK CORPORATION (FOREIGN)`'),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CFNR'), (
        'label', 'REGISTRATION OF CORPORATE NAME FOR FOREIGN CORPORATIONS (STOCK & NON-STOCK)'), ('stock', 'TRUE'),
                                          ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
                                          ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CFNRR'),
         ('label', 'RENEWAL OF REGISTRATION OF CORPORATE NAME FOR FOREIGN CORPORATIONS (STOCK & NON-STOCK)'),
         ('stock', 'TRUE'), ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CFRIS'), (
        'label', 'CERTIFICATE OF RE-DOMESTICATION FOR STOCK INSURANCE CHANGE FROM FOREIGN TO DOMESTIC'),
                                          ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'),
                                          ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'INS')]),
            OrderedDict([('cd_trans_type', 'CFRN'), ('label', 'ANNUAL REPORT FOR FOREIGN NON-STOCK CORPORATION'),
                         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
                         ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CFRO'), (
        'label', 'CERTIFICATE OF RE-DOMESTICATION FOR STOCK INSURANCE CHANGE FROM DOMESTIC TO FOREIGN'),
                                                                                ('stock', 'TRUE'),
                                                                                ('nonstock', 'FALSE'),
                                                                                ('domestic', 'FALSE'),
                                                                                ('foreign_company', 'TRUE'),
                                                                                ('benefit', 'FALSE'),
                                                                                ('company_type', 'INS')]), OrderedDict(
        [('cd_trans_type', 'CFRS'), ('label', 'ANNUAL REPORT FOR FOREIGN STOCK CORPORATION'), ('stock', 'TRUE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CFRSX'), ('label', 'CORRECTED REPORT FOR FOREIGN STOCK CORPORATION '),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CFWN'), ('label', 'WITHDRAWAL FOR NON-STOCK CORPORATION (FOREIGN) '),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CFWS'), ('label', 'WITHDRAWAL FOR STOCK CORPORATION (FOREIGN) '), ('stock', 'TRUE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CICUN'), ('label', 'BUSINESS FORMATION FOR DOMESTIC CREDIT UNION (NON-STOCK)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CU')]), OrderedDict(
        [('cd_trans_type', 'CIN'), ('label', 'BUSINESS FORMATION FOR NON-STOCK CORPORATION (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CIS'), ('label', 'BUSINESS FORMATION FOR STOCK CORPORATION (DOMESTIC)'),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'COCN'), (
        'label', 'CORRECTED ORGANIZATION AND FIRST REPORT FOR DOMESTIC NON-STOCK CORPORATION'), ('stock', 'FALSE'),
                                          ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                                          ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'COCS'),
         ('label', 'CORRECTED ORGANIZATION AND FIRST REPORT FOR DOMESTIC STOCK CORPORATION'), ('stock', 'TRUE'),
         ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CON'), ('label', 'ORGANIZATION AND FIRST REPORT FOR NON-STOCK CORPORATION (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'COS'), ('label', 'ORGANIZATION AND FIRST REPORT FOR STOCK CORPORATION (DOMESTIC)'),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CRCA'), ('label', 'BUSINESS AMENDMENT FOR RELIGIOUS (NON-STOCK)'), ('stock', 'FALSE'),
         ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'REL')]),
            OrderedDict([('cd_trans_type', 'CRDN'),
                         ('label', 'REVOCATION OF DISSOLUTION  FOR NON-STOCK CORPORATION (DOMESTIC)'),
                         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CRDS'), ('label', 'REVOCATION OF DISSOLUTION  FOR STOCK CORPORATION (DOMESTIC)'),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CRLC'), ('label', 'ANNUAL REPORT FOR LIMITED LIABILITY COMPANY (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'CRLCF'), ('label', 'ANNUAL REPORT FOR LIMITED LIABILITY COMPANY (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'CRLLP'), ('label', 'ANNUAL REPORT FOR LIMITED LIABILITY PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'CRLLPF'), ('label', 'ANNUAL REPORT FOR LIMITED LIABILITY PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'CRLP'), ('label', 'ANNUAL REPORT FOR LIMITED PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'CRLPF'), ('label', 'ANNUAL REPORT FOR LIMITED PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'CRN'), ('label', 'ANNUAL REPORT FOR NON-STOCK CORPORATION (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CRNX'), ('label', 'CORRECTED REPORT FOR DOMESTIC NON-STOCK CORPORATION'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CRSX'), ('label', 'CORRECTED REPORT FOR DOMESTIC STOCK CORPORATION '),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CSCSS'), (
        'label', 'CERTIFICATE OF SURRENDER FOR OTHER STOCK CORPORATIONS (CREDIT UNION)'), ('stock', 'TRUE'),
                                          ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
                                          ('benefit', 'FALSE'), ('company_type', 'CU')]), OrderedDict(
        [('cd_trans_type', 'CUAN'),
         ('label', 'CERTIFICATE OF AMENDMENT FOR OTHER NON STOCK CORPORATION (CREDIT UNION)'), ('stock', 'FALSE'),
         ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'CU')]),
            OrderedDict([('cd_trans_type', 'CZLC'),
                         ('label', 'CERTIFICATE OF REINSTATEMENT FOR LIMITED LIABILITY COMPANY (DOMESTIC)'),
                         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict([('cd_trans_type', 'CZLCN'), (
        'label', 'CERTIFICATE OF REINSTATEMENT FOR DOMESTIC LIMITED LIABILITY COMPANY WITH NAME CHANGE '),
                                                                               ('stock', 'FALSE'),
                                                                               ('nonstock', 'FALSE'),
                                                                               ('domestic', 'TRUE'),
                                                                               ('foreign_company', 'FALSE'),
                                                                               ('benefit', 'FALSE'),
                                                                               ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'CZLP'),
         ('label', 'CERTIFICATE OF REINSTATEMENT FOR DOMESTIC LIMITED PARTNERSHIP WITHOUT NAME CHANGE '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'CZN'), ('label', 'CERTIFICATE OF REINSTATEMENT FOR NON-STOCK CORPORATION (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CZNN'), (
        'label', 'CERTIFICATE OF REINSTATEMENT FOR DOMESTIC NON-STOCK CORPORATION WITH NAME CHANGE '),
                                          ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'),
                                          ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'CORP')]),
            OrderedDict([('cd_trans_type', 'CZNPO'), ('label',
                                                      'CERTIFICATE OF REINSTATEMENT FOR DOMESTIC NON-STOCK AND FIRST ORGANIZATION & REPORT WITHOUT NAME CHANGE '),
                         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CZNPON'), (
        'label',
        'CERTIFICATE OF REINSTATEMENT FOR DOMESTIC NON-STOCK AND FIRST ORGANIZATION & REPORT WITH NAME CHANGE '),
                                                                                ('stock', 'FALSE'),
                                                                                ('nonstock', 'TRUE'),
                                                                                ('domestic', 'TRUE'),
                                                                                ('foreign_company', 'FALSE'),
                                                                                ('benefit', 'FALSE'),
                                                                                ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CZS'), ('label', 'CERTIFICATE OF REINSTATEMENT FOR STOCK CORPORATION (DOMESTIC)'),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CZSN'), (
        'label', 'CERTIFICATE OF REINSTATEMENT FOR DOMESTIC STOCK CORPORATION WITHOUT NAME CHANGE '), ('stock', 'TRUE'),
                                          ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                                          ('benefit', 'FALSE'), ('company_type', 'CORP')]), OrderedDict(
        [('cd_trans_type', 'CZSPO'), ('label',
                                      'CERTIFICATE OF REINSTATEMENT FOR DOMESTIC STOCK AND FIRST ORGANIZATION & REPORT WITHOUT NAME CHANGE '),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'CORP')]), OrderedDict([('cd_trans_type', 'CZSPON'), (
        'label', 'CERTIFICATE OF REINSTATEMENT FOR DOMESTIC STOCK AND FIRST ORGANIZATION & REPORT WITH NAME CHANGE '),
                                          ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'),
                                          ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'CORP')]),
            OrderedDict([('cd_trans_type', 'GP'), (
                'label', 'STATEMENT OF PARTNERSHIP AUTHORITY (GENERAL PARTNERSHIP) [PARTNERSHIP FORMATION]'),
                         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', 'GP')]), OrderedDict(
        [('cd_trans_type', 'GPA'), ('label', 'BUSINESS AMENDMENT FOR GENERAL PARTNERSHIP'), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'GP')]),
            OrderedDict([('cd_trans_type', 'GPC'), ('label', 'STATEMENT OF CANCELLATION FOR GENERAL PARTNERSHIP'),
                         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', 'GP')]), OrderedDict(
        [('cd_trans_type', 'GPDIS'), ('label', 'STATEMENT OF DISSOLUTION FOR GENERAL PARTNERSHIP'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'GP')]), OrderedDict(
        [('cd_trans_type', 'GPDISA'), ('label', 'STATEMENT OF DISSOCIATION FOR LIMITED PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'IAS'), ('label', 'INCORPORATION AMENDMENT OF A STOCK INSURANCE COMPANY'),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'INS')]), OrderedDict(
        [('cd_trans_type', 'IN'), ('label', 'BUSINESS FORMATION FOR DOMESTIC INSURANCE (NON-STOCK)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'INS')]), OrderedDict(
        [('cd_trans_type', 'IS'), ('label', 'BUSINESS FORMATION FOR DOMESTIC INSURANCE (STOCK)'), ('stock', 'TRUE'),
         ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', 'INS')]),
            OrderedDict(
                [('cd_trans_type', 'LC'), ('label', 'BUSINESS FORMATION FOR LIMITED LIABILITY COMPANY (DOMESTIC)'),
                 ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                 ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCA'), ('label', 'BUSINESS AMENDMENTS FOR LIMITED LIABILITY COMPANY (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCAA'), ('label', 'AGENT ADDRESS CHANGE FOR LIMITED LIABILITY COMPANY (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCAC'), ('label', 'AGENT CHANGE FOR LIMITED LIABILITY COMPANY (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCACM'), ('label', 'BUSINESS ADDRESS CHANGE FOR LIMITED LIABILITY COMPANY (DOMESTIC) '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCAR'), ('label', 'RESIGNATION OF AGENT  FOR LIMITED LIABILITY COMPANY (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict([('cd_trans_type', 'LCCO'), (
        'label', 'CERTIFICATE OF CONSOLIDATION FOR LIMITED LIABILITY COMPANY (DOMESTIC)'), ('stock', 'FALSE'),
                                                               ('nonstock', 'FALSE'), ('domestic', 'TRUE'),
                                                               ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
                                                               ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCD'), ('label', 'BUSINESS DISSOLUTION FOR LIMITED LIABILITY COMPANY (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCF'), ('label', 'BUSINESS FORMATION FOR LIMITED LIABILITY COMPANY (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCFA'), ('label', 'BUSINESS AMENDMENTS FOR LIMITED LIABILITY COMPANY (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCFAA'), ('label', 'AGENT ADDRESS CHANGE FOR LIMITED LIABILITY COMPANY (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCFAC'), ('label', 'AGENT CHANGE FOR LIMITED LIABILITY COMPANY (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCFACM'), ('label', 'BUSINESS ADDRESS CHANGE FOR LIMITED LIABILITY COMPANY (FOREIGN) '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCFAR'), ('label', 'RESIGNATION OF AGENT  FOR LIMITED LIABILITY COMPANY (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LLC')]), OrderedDict([('cd_trans_type', 'LCFC'), (
        'label', 'CERTIFICATE OF CANCELLATION FOR  LIMITED LIABILITY COMPANY (FOREIGN)'), ('stock', 'FALSE'),
                                                               ('nonstock', 'FALSE'), ('domestic', 'FALSE'),
                                                               ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
                                                               ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LCINC'),
         ('label', 'INTERIM NOTICE FOR LIMITED LIABILITY COMPANY (DOMESTIC OR FOREIGN)'), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'LLC')]), OrderedDict(
        [('cd_trans_type', 'LLP'), ('label', 'BUSINESS FORMATION FOR LIMITED LIABILITY PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'LLPA'), ('label', 'BUSINESS AMENDMENT FOR LIMITED LIABILITY PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'LLPAC'), ('label', 'AGENT CHANGE  FOR LIMITED LIABILITY PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict([('cd_trans_type', 'LLPACM'), (
        'label', 'BUSINESS ADDRESS CHANGE FOR LIMITED LIABILITY PARTNERSHIP (DOMESTIC) '), ('stock', 'FALSE'),
                                                               ('nonstock', 'FALSE'), ('domestic', 'TRUE'),
                                                               ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
                                                               ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'LLPF'), ('label', 'BUSINESS FORMATION FOR LIMITED LIABILITY PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'LLPFA'), ('label', 'BUSINESS AMENDMENT FOR LIMITED LIABILITY PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict([('cd_trans_type', 'LLPFAA'), (
        'label', 'AGENT ADDRESS CHANGE  FOR LIMITED LIABILITY PARTNERSHIP (FOREIGN)'), ('stock', 'FALSE'),
                                                               ('nonstock', 'FALSE'), ('domestic', 'TRUE'),
                                                               ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
                                                               ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'LLPFAC'), ('label', 'AGENT CHANGE  FOR LIMITED LIABILITY PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict([('cd_trans_type', 'LLPFACM'), (
        'label', 'BUSINESS ADDRESS CHANGE FOR LIMITED LIABILITY PARTNERSHIP (FOREIGN) '), ('stock', 'FALSE'),
                                                               ('nonstock', 'FALSE'), ('domestic', 'TRUE'),
                                                               ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
                                                               ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'LLPFAR'), ('label', 'RESIGNATION OF AGENT FOR LIMITED LIABILITY PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict([('cd_trans_type', 'LLPFW'), (
        'label', 'CERTIFICATE OF WITHDRAWAL FOR LIMITED LIABILITY PARTNERSHIP (FOREIGN)'), ('stock', 'FALSE'),
                                                               ('nonstock', 'FALSE'), ('domestic', 'TRUE'),
                                                               ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
                                                               ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'LLPM'),
         ('label', 'CERTIFICATE OF MERGER FOR DOMESTIC & FOREIGN LIMITED LIABILITY PARTNERSHIP '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'LLP')]), OrderedDict([('cd_trans_type', 'LLPR'), (
        'label', 'RENUNCIATION OF STATUS REPORT FOR LIMITED LIABILITY PARTNERSHIP (DOMESTIC)'), ('stock', 'FALSE'),
                                         ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                                         ('benefit', 'FALSE'), ('company_type', 'LLP')]), OrderedDict(
        [('cd_trans_type', 'LP'), ('label', 'BUSINESS FORMATION FOR LIMITED PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPA'), ('label', 'BUSINESS AMENDMENT  FOR LIMITED PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPAA'), ('label', 'AGENT ADDRESS CHANGE  FOR LIMITED PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPAC'), ('label', 'AGENT CHANGE  FOR LIMITED PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPACM'), ('label', 'BUSINESS ADDRESS CHANGE FOR LIMITED PARTNERSHIP (DOMESTIC) '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPAR'), ('label', 'RESIGNATION OF AGENT  FOR LIMITED PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPC'), ('label', 'CERTIFICATE OF CANCELLATION  FOR LIMITED PARTNERSHIP (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPF'), ('label', 'BUSINESS FORMATION FOR LIMITED PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPFA'), ('label', 'BUSINESS AMENDMENT  FOR LIMITED PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPFAA'), ('label', 'AGENT ADDRESS CHANGE  FOR LIMITED PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPFAC'), ('label', 'AGENT CHANGE  FOR LIMITED PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPFACM'), ('label', 'BUSINESS ADDRESS CHANGE FOR LIMITED PARTNERSHIP (FOREIGN) '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPFAR'), ('label', 'RESIGNATION OF AGENT  FOR LIMITED PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'LPFC'), ('label', 'CERTIFICATE OF CANCELLATION  FOR LIMITED PARTNERSHIP (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'LP')]), OrderedDict(
        [('cd_trans_type', 'ST'), ('label', 'BUSINESS FORMATION FOR STATUTORY TRUST (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STA'), ('label', 'BUSINESS AMENDMENT FOR STATUTORY TRUST (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STAC'), ('label', 'AGENT CHANGE FOR STATUTORY TRUST (DOMESTIC)'), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STACM'), ('label', 'BUSINESS ADDRESS CHANGE FOR STATUTORY TRUST (DOMESTIC) '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STAR'), ('label', 'RESIGNATION OF AGENT FOR STATUTORY TRUST (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STC'), ('label', 'CERTIFICATE OF CANCELLATION FOR STATUTORY TRUST (DOMESTIC)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STF'), ('label', 'BUSINESS FORMATION FOR STATUTORY TRUST (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STFA'), ('label', 'BUSINESS AMENDMENT FOR STATUTORY TRUST (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STFAA'), ('label', 'AGENT ADDRESS CHANGE FOR STATUTORY TRUST (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STFAC'), ('label', 'AGENT CHANGE FOR STATUTORY TRUST (FOREIGN)'), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STFACM'), ('label', 'BUSINESS ADDRESS CHANGE FOR STATUTORY TRUST (FOREIGN) '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STFAR'), ('label', 'RESIGNATION OF AGENT FOR STATUTORY TRUST (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STFC'), ('label', 'CERTIFICATE OF CANCELLATION FOR STATUTORY TRUST (FOREIGN)'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'TRUE'),
         ('benefit', 'FALSE'), ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'STM'), ('label', 'CERTIFICATE OF MERGER FOR STATUTORY TRUST '), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
         ('company_type', 'STAT')]), OrderedDict(
        [('cd_trans_type', 'CCNR'), ('label', 'CANCELLATION OF NAME RESERVATION FOR ALL ENTITIES'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'TRUE'),
         ('company_type', '')]), OrderedDict([('cd_trans_type', 'ACM'), ('label',
                                                                 'BUSINESS ADDRESS CHANGE FOR CORPORATIONS, LIMITED PARTNERSHIP, LIMITED LIABILITY COMPANY, LIMITED LIABILITY PARTNERSHIP, STATUTARY TRUST (DOMESTIC & FOREIGN) [INCLUDING BENEFIT CORPORATION]'),
                                      ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'TRUE'),
                                      ('foreign_company', 'TRUE'), ('benefit', 'TRUE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'XOVRB'), ('label', 'TRANSACTION TYPE FOR OVERRIDE FILING IN LAGACY'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'RSHR'), ('label', 'RETIREMENT OF SHARES'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'NOTC'), ('label',
                                     'BULK NOTICES ARE FILING FROM LEGACY APPLICATION AND THESE DETAILS ARE SHOWING IN ADMINSTRATIVE DISSOLUTION'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'MSC'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'MISC'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'LPM'),
         ('label', 'CERTIFICATE OF MERGER FOR DOMESTIC & FOREIGN NON LIMITED PARTNERSHIP '), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'), ('company_type', '')]),
            OrderedDict([('cd_trans_type', 'LPLC'),
                         ('label', 'CERTIFICATE OF MERGER FOR DOMESTIC & FOREIGN NON LIMITED PARTNERSHIP'),
                         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
                         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'LLPLC'), ('label', 'ORGANIZATION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'LFCAA'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'LFC'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'LFACM'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'LCM'),
         ('label', 'CERTIFICATE OF MERGER FOR DOMESTIC & FOREIGN NON LIMITED LIABILITY COMPANY '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'IASC'), ('label', 'AMENDMENT'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'IANC'), ('label', 'AMENDMENT'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'GPCGPLP'),
         ('label', 'STATEMENT OF CONVERSION FROM GENERAL PARTNERSHIP TO DOMESTIC LIMITED PARTNERSHIP'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict([('cd_trans_type', 'GPCGPLC'), (
        'label', 'STATEMENT OF CONVERSION FROM GENERAL PARTNERSHIP TO DOMESTIC LIMITED LIABILITY COMPANY'),
                                                            ('stock', 'FALSE'), ('nonstock', 'FALSE'),
                                                            ('domestic', 'TRUE'), ('foreign_company', 'FALSE'),
                                                            ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'FFTD'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CXMB'), ('label', 'MISCELLANEOUS'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CVN'), ('label', 'CONVERSION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CV'), ('label', 'CONVERSION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CUANC'), ('label', 'AMENDMENT'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CSES'), ('label', 'SHARE EXCHANGE'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CPCS'), ('label', 'ADDITIONAL PRINCIPAL'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CPCN'), ('label', 'CEASE PRINCIPAL'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'COSCA'), ('label', 'ORGANIZATION AND FIRST REPORT'), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]),
            OrderedDict(
                [('cd_trans_type', 'COR'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
                 ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CNSL'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CNRT'), ('label', 'TRANSFER OF RESERVED NAME FOR ALL ENTITIES'), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]),
            OrderedDict(
                [('cd_trans_type', 'CNR'), ('label', 'NAME RESERVATION FOR ALL ENTITIES'), ('stock', 'FALSE'),
                 ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
                 ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CMSL'), ('label', 'NOT PROVIDED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CMSC'), ('label', 'MERGER'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CMS'), ('label', 'CERTIFICATE OF MERGER FOR DOMESTIC & FOREIGN STOCK CORPORATION '),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'),
         ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CMNC'), ('label', 'MERGER'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CMIS'), ('label', 'MISCELLANEOUS'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CISCS'), ('label', 'CERTIFICATE OF CREDIT UNION FOR STOCK CORPORATION (IN LEGACY)'),
         ('stock', 'TRUE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CISCA'), ('label', 'INCORPORATED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CICR'), ('label', 'INCORPORATED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CICC'), ('label', 'INCORPORATED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CFNC'), ('label', 'INCORPORATED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CFN'), ('label', 'INCORPORATED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CES'), ('label', 'ADDITIONAL PRINCIPAL'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CEN'), ('label', 'ADDITIONAL PRINCIPAL'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CDRSPO'), ('label', 'DISSOLUTION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CDRNPO'), ('label', 'DISSOLUTION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CDES'), ('label', 'DISSOLUTION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CDEN'), ('label', 'DISSOLUTION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CCSAO'), ('label', 'CONSOLIDATION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CCSA'), ('label', 'CONSOLIDATION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CCORS'),
         ('label', 'CERTIFICATE OF CORRECTION FOR STOCK CORPORATIONS (DOMESTIC & FOREIGN)'), ('stock', 'TRUE'),
         ('nonstock', 'FALSE'), ('domestic', 'TRUE'), ('foreign_company', 'TRUE'), ('benefit', 'FALSE'), ('company_type', '')]),
            OrderedDict(
                [('cd_trans_type', 'CCNAO'), ('label', 'CONSOLIDATION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
                 ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CCNA'), ('label', 'CONSOLIDATION'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CCAS'), ('label', 'ABANDONMENT'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CCANL'), ('label', 'CANCELLATION OF SHARES'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CASC'), ('label', 'AMENDMENT'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CANC'), ('label', 'AMENDMENT'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'BT'), ('label', 'INCORPORATED'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'BRVKD'), ('label', 'ON DEMAND BATCH PROGRAM FOR BULK FILING FOR REVOKED'),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'BFFTD'), ('label', 'ON DEMAND BATCH PROGRAM FOR BULK FILING FOR FORFEITED '),
         ('stock', 'FALSE'), ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'BASC'), ('label', 'AMENDMENT'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'BANC'), ('label', 'AMENDMENT'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'BAADDR'), ('label', 'BULK FILING CHANGE AGENT ADDRESS BATCH JOB'), ('stock', 'FALSE'),
         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')]),
            OrderedDict([('cd_trans_type', 'BAADD'), ('label', 'AGENT ADDRESS CHANGE'), ('stock', 'FALSE'),
                         ('nonstock', 'FALSE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'),
                         ('company_type', '')]), OrderedDict([('cd_trans_type', 'CFRIN'), (
        'label', 'CERTIFICATE OF RE-DOMESTICATION FOR NON-STOCK INSURANCE CHANGE FROM FOREIGN TO DOMESTIC'),
                                                      ('stock', 'FALSE'), ('nonstock', 'TRUE'),
                                                      ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
                                                      ('benefit', 'FALSE'), ('company_type', 'INS')]), OrderedDict(
        [('cd_trans_type', 'CISCN'), ('label', 'CERTIFICATE OF CREDIT UNION FOR NON STOCK CORPORATION (IN LEGACY)'),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'CMN'), ('label', 'CERTIFICATE OF MERGER FOR DOMESTIC & FOREIGN NON STOCK CORPORATION '),
         ('stock', 'FALSE'), ('nonstock', 'TRUE'), ('domestic', 'FALSE'), ('foreign_company', 'FALSE'),
         ('benefit', 'FALSE'), ('company_type', '')]), OrderedDict(
        [('cd_trans_type', 'XPREBFALSE'), ('label', 'FALSE'), ('stock', 'FALSE'), ('nonstock', 'FALSE'),
         ('domestic', 'FALSE'), ('foreign_company', 'FALSE'), ('benefit', 'FALSE'), ('company_type', '')])]

fips = [OrderedDict([('town', 'Connecticut'), ('fips', '09'), ('county_fips', '09'), ('county', 'Connecticut'),
                     ('subtown', 'Connecticut')]), OrderedDict(
    [('town', 'Bethel'), ('fips', '0900104720'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Bethel')]), OrderedDict(
    [('town', 'Bridgeport'), ('fips', '0900108070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Bridgeport')]), OrderedDict(
    [('town', 'Brookfield'), ('fips', '0900108980'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Brookfield')]), OrderedDict(
    [('town', 'Danbury'), ('fips', '0900118500'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Danbury')]), OrderedDict(
    [('town', 'Darien'), ('fips', '0900118850'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Darien')]), OrderedDict(
    [('town', 'Easton'), ('fips', '0900123890'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Easton')]), OrderedDict(
    [('town', 'Fairfield'), ('fips', '0900126620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Fairfield')]), OrderedDict(
    [('town', 'Greenwich'), ('fips', '0900133620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Greenwich')]), OrderedDict(
    [('town', 'Monroe'), ('fips', '0900148620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Monroe')]), OrderedDict(
    [('town', 'New Canaan'), ('fips', '0900150580'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'New Canaan')]), OrderedDict(
    [('town', 'New Fairfield'), ('fips', '0900150860'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'New Fairfield')]), OrderedDict(
    [('town', 'Newtown'), ('fips', '0900152980'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Newtown')]), OrderedDict(
    [('town', 'Norwalk'), ('fips', '0900156060'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Norwalk')]), OrderedDict(
    [('town', 'Redding'), ('fips', '0900163480'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Redding')]), OrderedDict(
    [('town', 'Ridgefield'), ('fips', '0900163970'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Ridgefield')]), OrderedDict(
    [('town', 'Shelton'), ('fips', '0900168170'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Shelton')]), OrderedDict(
    [('town', 'Sherman'), ('fips', '0900168310'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Sherman')]), OrderedDict(
    [('town', 'Stamford'), ('fips', '0900173070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Stamford')]), OrderedDict(
    [('town', 'Stratford'), ('fips', '0900174190'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Stratford')]), OrderedDict(
    [('town', 'Trumbull'), ('fips', '0900177200'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Trumbull')]), OrderedDict(
    [('town', 'Weston'), ('fips', '0900183430'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Weston')]), OrderedDict(
    [('town', 'Westport'), ('fips', '0900183500'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Westport')]), OrderedDict(
    [('town', 'Wilton'), ('fips', '0900186370'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Wilton')]), OrderedDict(
    [('town', 'Avon'), ('fips', '0900302060'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Avon')]), OrderedDict(
    [('town', 'Berlin'), ('fips', '0900304300'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Berlin')]), OrderedDict(
    [('town', 'Bloomfield'), ('fips', '0900305910'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Bloomfield')]), OrderedDict(
    [('town', 'Bristol'), ('fips', '0900308490'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Bristol')]), OrderedDict(
    [('town', 'Burlington'), ('fips', '0900310100'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Burlington')]), OrderedDict(
    [('town', 'Canton'), ('fips', '0900312270'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Canton')]), OrderedDict(
    [('town', 'East Granby'), ('fips', '0900322070'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'East Granby')]), OrderedDict(
    [('town', 'East Hartford'), ('fips', '0900322630'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'East Hartford')]), OrderedDict(
    [('town', 'East Windsor'), ('fips', '0900324800'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'East Windsor')]), OrderedDict(
    [('town', 'Enfield'), ('fips', '0900325990'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Enfield')]), OrderedDict(
    [('town', 'Farmington'), ('fips', '0900327600'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Farmington')]), OrderedDict(
    [('town', 'Glastonbury'), ('fips', '0900331240'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Glastonbury')]), OrderedDict(
    [('town', 'Granby'), ('fips', '0900332640'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Granby')]), OrderedDict(
    [('town', 'Hartford'), ('fips', '0900337070'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Hartford')]), OrderedDict(
    [('town', 'Hartland'), ('fips', '0900337140'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Hartland')]), OrderedDict(
    [('town', 'Manchester'), ('fips', '0900344700'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Manchester')]), OrderedDict(
    [('town', 'Marlborough'), ('fips', '0900345820'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Marlborough')]), OrderedDict(
    [('town', 'New Britain'), ('fips', '0900350440'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'New Britain')]), OrderedDict(
    [('town', 'Newington'), ('fips', '0900352140'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Newington')]), OrderedDict(
    [('town', 'Plainville'), ('fips', '0900360120'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Plainville')]), OrderedDict(
    [('town', 'Rocky Hill'), ('fips', '0900365370'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Rocky Hill')]), OrderedDict(
    [('town', 'Simsbury'), ('fips', '0900368940'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Simsbury')]), OrderedDict(
    [('town', 'Southington'), ('fips', '0900370550'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Southington')]), OrderedDict(
    [('town', 'South Windsor'), ('fips', '0900371390'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'South Windsor')]), OrderedDict(
    [('town', 'Suffield'), ('fips', '0900374540'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Suffield')]), OrderedDict(
    [('town', 'West Hartford'), ('fips', '0900382590'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'West Hartford')]), OrderedDict(
    [('town', 'Wethersfield'), ('fips', '0900384900'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Wethersfield')]), OrderedDict(
    [('town', 'Windsor'), ('fips', '0900387000'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Windsor')]), OrderedDict(
    [('town', 'Windsor Locks'), ('fips', '0900387070'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Windsor Locks')]), OrderedDict(
    [('town', 'Barkhamsted'), ('fips', '0900502760'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Barkhamsted')]), OrderedDict(
    [('town', 'Bethlehem'), ('fips', '0900504930'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Bethlehem')]), OrderedDict(
    [('town', 'Bridgewater'), ('fips', '0900508210'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Bridgewater')]), OrderedDict(
    [('town', 'Canaan'), ('fips', '0900510940'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Canaan')]), OrderedDict(
    [('town', 'Colebrook'), ('fips', '0900516050'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Colebrook')]), OrderedDict(
    [('town', 'Cornwall'), ('fips', '0900517240'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Cornwall')]), OrderedDict(
    [('town', 'Goshen'), ('fips', '0900532290'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Goshen')]), OrderedDict(
    [('town', 'Harwinton'), ('fips', '0900537280'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Harwinton')]), OrderedDict(
    [('town', 'Kent'), ('fips', '0900540290'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Kent')]), OrderedDict(
    [('town', 'Litchfield'), ('fips', '0900543370'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Litchfield')]), OrderedDict(
    [('town', 'Morris'), ('fips', '0900549460'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Morris')]), OrderedDict(
    [('town', 'New Hartford'), ('fips', '0900551350'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'New Hartford')]), OrderedDict(
    [('town', 'New Milford'), ('fips', '0900552630'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'New Milford')]), OrderedDict(
    [('town', 'Norfolk'), ('fips', '0900553470'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Norfolk')]), OrderedDict(
    [('town', 'North Canaan'), ('fips', '0900554030'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'North Canaan')]), OrderedDict(
    [('town', 'Plymouth'), ('fips', '0900560750'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Plymouth')]), OrderedDict(
    [('town', 'Roxbury'), ('fips', '0900565930'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Roxbury')]), OrderedDict(
    [('town', 'Salisbury'), ('fips', '0900566420'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Salisbury')]), OrderedDict(
    [('town', 'Sharon'), ('fips', '0900567960'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Sharon')]), OrderedDict(
    [('town', 'Thomaston'), ('fips', '0900575730'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Thomaston')]), OrderedDict(
    [('town', 'Torrington'), ('fips', '0900576570'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Torrington')]), OrderedDict(
    [('town', 'Warren'), ('fips', '0900579510'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Warren')]), OrderedDict(
    [('town', 'Washington'), ('fips', '0900579720'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Washington')]), OrderedDict(
    [('town', 'Watertown'), ('fips', '0900580490'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Watertown')]), OrderedDict(
    [('town', 'Winchester'), ('fips', '0900586440'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Winchester')]), OrderedDict(
    [('town', 'Woodbury'), ('fips', '0900587910'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Woodbury')]), OrderedDict(
    [('town', 'Chester'), ('fips', '0900714300'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Chester')]), OrderedDict(
    [('town', 'Clinton'), ('fips', '0900715350'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Clinton')]), OrderedDict(
    [('town', 'Cromwell'), ('fips', '0900718080'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Cromwell')]), OrderedDict(
    [('town', 'Deep River'), ('fips', '0900719130'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Deep River')]), OrderedDict(
    [('town', 'Durham'), ('fips', '0900720810'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Durham')]), OrderedDict(
    [('town', 'East Haddam'), ('fips', '0900722280'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'East Haddam')]), OrderedDict(
    [('town', 'East Hampton'), ('fips', '0900722490'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'East Hampton')]), OrderedDict(
    [('town', 'Essex'), ('fips', '0900726270'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Essex')]), OrderedDict(
    [('town', 'Haddam'), ('fips', '0900735230'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Haddam')]), OrderedDict(
    [('town', 'Killingworth'), ('fips', '0900740710'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Killingworth')]), OrderedDict(
    [('town', 'Middlefield'), ('fips', '0900747080'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Middlefield')]), OrderedDict(
    [('town', 'Middletown'), ('fips', '0900747360'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Middletown')]), OrderedDict(
    [('town', 'Old Saybrook'), ('fips', '0900757320'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Old Saybrook')]), OrderedDict(
    [('town', 'Portland'), ('fips', '0900761800'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Portland')]), OrderedDict(
    [('town', 'Westbrook'), ('fips', '0900781680'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Westbrook')]), OrderedDict(
    [('town', 'Ansonia'), ('fips', '0900901220'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Ansonia')]), OrderedDict(
    [('town', 'Beacon Falls'), ('fips', '0900903250'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Beacon Falls')]), OrderedDict(
    [('town', 'Bethany'), ('fips', '0900904580'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Bethany')]), OrderedDict(
    [('town', 'Branford'), ('fips', '0900907310'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Branford')]), OrderedDict(
    [('town', 'Cheshire'), ('fips', '0900914160'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Cheshire')]), OrderedDict(
    [('town', 'Derby'), ('fips', '0900919550'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Derby')]), OrderedDict(
    [('town', 'East Haven'), ('fips', '0900922910'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'East Haven')]), OrderedDict(
    [('town', 'Guilford'), ('fips', '0900934950'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Guilford')]), OrderedDict(
    [('town', 'Hamden'), ('fips', '0900935650'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Hamden')]), OrderedDict(
    [('town', 'Madison'), ('fips', '0900944560'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Madison')]), OrderedDict(
    [('town', 'Meriden'), ('fips', '0900946520'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Meriden')]), OrderedDict(
    [('town', 'Middlebury'), ('fips', '0900946940'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Middlebury')]), OrderedDict(
    [('town', 'Milford'), ('fips', '0900947535'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Milford')]), OrderedDict(
    [('town', 'Naugatuck'), ('fips', '0900949950'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Naugatuck')]), OrderedDict(
    [('town', 'New Haven'), ('fips', '0900952070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'New Haven')]), OrderedDict(
    [('town', 'North Branford'), ('fips', '0900953890'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'North Branford')]), OrderedDict(
    [('town', 'North Haven'), ('fips', '0900954870'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'North Haven')]), OrderedDict(
    [('town', 'Orange'), ('fips', '0900957600'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Orange')]), OrderedDict(
    [('town', 'Oxford'), ('fips', '0900958300'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Oxford')]), OrderedDict(
    [('town', 'Prospect'), ('fips', '0900962290'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Prospect')]), OrderedDict(
    [('town', 'Seymour'), ('fips', '0900967610'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Seymour')]), OrderedDict(
    [('town', 'Southbury'), ('fips', '0900969640'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Southbury')]), OrderedDict(
    [('town', 'Wallingford'), ('fips', '0900978740'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Wallingford')]), OrderedDict(
    [('town', 'Waterbury'), ('fips', '0900980070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Waterbury')]), OrderedDict(
    [('town', 'West Haven'), ('fips', '0900982870'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'West Haven')]), OrderedDict(
    [('town', 'Wolcott'), ('fips', '0900987560'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Wolcott')]), OrderedDict(
    [('town', 'Woodbridge'), ('fips', '0900987700'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Woodbridge')]), OrderedDict(
    [('town', 'Bozrah'), ('fips', '0901106820'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Bozrah')]), OrderedDict(
    [('town', 'Colchester'), ('fips', '0901115910'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Colchester')]), OrderedDict(
    [('town', 'East Lyme'), ('fips', '0901123400'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'East Lyme')]), OrderedDict(
    [('town', 'Franklin'), ('fips', '0901129910'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Franklin')]), OrderedDict(
    [('town', 'Griswold'), ('fips', '0901133900'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Griswold')]), OrderedDict(
    [('town', 'Groton'), ('fips', '0901134250'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Groton')]), OrderedDict(
    [('town', 'Lebanon'), ('fips', '0901142390'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Lebanon')]), OrderedDict(
    [('town', 'Ledyard'), ('fips', '0901142600'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Ledyard')]), OrderedDict(
    [('town', 'Lisbon'), ('fips', '0901143230'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Lisbon')]), OrderedDict(
    [('town', 'Lyme'), ('fips', '0901144210'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Lyme')]), OrderedDict(
    [('town', 'Montville'), ('fips', '0901148900'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Montville')]), OrderedDict(
    [('town', 'New London'), ('fips', '0901152350'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'New London')]), OrderedDict(
    [('town', 'North Stonington'), ('fips', '0901155500'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'North Stonington')]), OrderedDict(
    [('town', 'Norwich'), ('fips', '0901156270'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Norwich')]), OrderedDict(
    [('town', 'Old Lyme'), ('fips', '0901157040'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Old Lyme')]), OrderedDict(
    [('town', 'Preston'), ('fips', '0901162150'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Preston')]), OrderedDict(
    [('town', 'Salem'), ('fips', '0901166210'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Salem')]), OrderedDict(
    [('town', 'Sprague'), ('fips', '0901171670'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Sprague')]), OrderedDict(
    [('town', 'Stonington'), ('fips', '0901173770'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Stonington')]), OrderedDict(
    [('town', 'Voluntown'), ('fips', '0901178600'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Voluntown')]), OrderedDict(
    [('town', 'Waterford'), ('fips', '0901180280'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Waterford')]), OrderedDict(
    [('town', 'Andover'), ('fips', '0901301080'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Andover')]), OrderedDict(
    [('town', 'Bolton'), ('fips', '0901306260'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Bolton')]), OrderedDict(
    [('town', 'Columbia'), ('fips', '0901316400'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Columbia')]), OrderedDict(
    [('town', 'Coventry'), ('fips', '0901317800'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Coventry')]), OrderedDict(
    [('town', 'Ellington'), ('fips', '0901325360'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Ellington')]), OrderedDict(
    [('town', 'Hebron'), ('fips', '0901337910'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Hebron')]), OrderedDict(
    [('town', 'Mansfield'), ('fips', '0901344910'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Mansfield')]), OrderedDict(
    [('town', 'Somers'), ('fips', '0901369220'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Somers')]), OrderedDict(
    [('town', 'Stafford'), ('fips', '0901372090'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Stafford')]), OrderedDict(
    [('town', 'Tolland'), ('fips', '0901376290'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Tolland')]), OrderedDict(
    [('town', 'Union'), ('fips', '0901377830'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Union')]), OrderedDict(
    [('town', 'Vernon'), ('fips', '0901378250'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Vernon')]), OrderedDict(
    [('town', 'Willington'), ('fips', '0901385950'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Willington')]), OrderedDict(
    [('town', 'Ashford'), ('fips', '0901501430'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Ashford')]), OrderedDict(
    [('town', 'Brooklyn'), ('fips', '0901509190'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Brooklyn')]), OrderedDict(
    [('town', 'Canterbury'), ('fips', '0901512130'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Canterbury')]), OrderedDict(
    [('town', 'Chaplin'), ('fips', '0901513810'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Chaplin')]), OrderedDict(
    [('town', 'Eastford'), ('fips', '0901521860'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Eastford')]), OrderedDict(
    [('town', 'Hampton'), ('fips', '0901536000'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Hampton')]), OrderedDict(
    [('town', 'Killingly'), ('fips', '0901540500'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Killingly')]), OrderedDict(
    [('town', 'Plainfield'), ('fips', '0901559980'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Plainfield')]), OrderedDict(
    [('town', 'Pomfret'), ('fips', '0901561030'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Pomfret')]), OrderedDict(
    [('town', 'Putnam'), ('fips', '0901562710'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Putnam')]), OrderedDict(
    [('town', 'Scotland'), ('fips', '0901567400'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Scotland')]), OrderedDict(
    [('town', 'Sterling'), ('fips', '0901573420'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Sterling')]), OrderedDict(
    [('town', 'Thompson'), ('fips', '0901575870'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Thompson')]), OrderedDict(
    [('town', 'Windham'), ('fips', '0901586790'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Windham')]), OrderedDict(
    [('town', 'Woodstock'), ('fips', '0901588190'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Woodstock')]), OrderedDict(
    [('town', 'Bridgeport'), ('fips', '0900108070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Barnum')]), OrderedDict(
    [('town', 'Bridgeport'), ('fips', '0900108070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Beardsley')]), OrderedDict(
    [('town', 'Bridgeport'), ('fips', '0900108070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Hillside')]), OrderedDict(
    [('town', 'Bridgeport'), ('fips', '0900108070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Newfield')]), OrderedDict(
    [('town', 'Bridgeport'), ('fips', '0900108070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Noble')]), OrderedDict(
    [('town', 'Brookfield'), ('fips', '0900108980'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Brookfield Center')]), OrderedDict(
    [('town', 'Danbury'), ('fips', '0900118500'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Candlewood')]), OrderedDict(
    [('town', 'Darien'), ('fips', '0900118850'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Noroton')]), OrderedDict(
    [('town', 'Darien'), ('fips', '0900118850'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Noroton Heights')]), OrderedDict(
    [('town', 'Fairfield'), ('fips', '0900126620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Samp Mortar')]), OrderedDict(
    [('town', 'Fairfield'), ('fips', '0900126620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Southport')]), OrderedDict(
    [('town', 'Greenwich'), ('fips', '0900133620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Banksville')]), OrderedDict(
    [('town', 'Greenwich'), ('fips', '0900133620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Byram')]), OrderedDict(
    [('town', 'Greenwich'), ('fips', '0900133620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Cos Cob')]), OrderedDict(
    [('town', 'Greenwich'), ('fips', '0900133620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Glenville')]), OrderedDict(
    [('town', 'Greenwich'), ('fips', '0900133620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Mianus')]), OrderedDict(
    [('town', 'Greenwich'), ('fips', '0900133620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Old Greenwich')]), OrderedDict(
    [('town', 'Greenwich'), ('fips', '0900133620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Riverside')]), OrderedDict(
    [('town', 'Monroe'), ('fips', '0900148620'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Stevenson')]), OrderedDict(
    [('town', 'Newtown'), ('fips', '0900152980'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Botsford')]), OrderedDict(
    [('town', 'Newtown'), ('fips', '0900152980'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Hawleyville')]), OrderedDict(
    [('town', 'Newtown'), ('fips', '0900152980'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Sandy Hook')]), OrderedDict(
    [('town', 'Norwalk'), ('fips', '0900156060'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Belden')]), OrderedDict(
    [('town', 'Norwalk'), ('fips', '0900156060'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Rowayton')]), OrderedDict(
    [('town', 'Norwalk'), ('fips', '0900156060'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'South Norwalk')]), OrderedDict(
    [('town', 'Norwalk'), ('fips', '0900156060'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'West Norwalk')]), OrderedDict(
    [('town', 'Norwalk'), ('fips', '0900156060'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'East Norwalk')]), OrderedDict(
    [('town', 'Redding'), ('fips', '0900163480'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Georgetown')]), OrderedDict(
    [('town', 'Redding'), ('fips', '0900163480'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Redding Ridge')]), OrderedDict(
    [('town', 'Redding'), ('fips', '0900163480'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'West Redding')]), OrderedDict(
    [('town', 'Shelton'), ('fips', '0900168170'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Huntington')]), OrderedDict(
    [('town', 'Shelton'), ('fips', '0900168170'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Pine Rock Park')]), OrderedDict(
    [('town', 'Stamford'), ('fips', '0900173070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Glenbrook')]), OrderedDict(
    [('town', 'Stamford'), ('fips', '0900173070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Ridgeway')]), OrderedDict(
    [('town', 'Stamford'), ('fips', '0900173070'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Springdale')]), OrderedDict(
    [('town', 'Westport'), ('fips', '0900183500'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Greens Farms')]), OrderedDict(
    [('town', 'Westport'), ('fips', '0900183500'), ('county_fips', '09001'), ('county', 'Fairfield County'),
     ('subtown', 'Saugatuck')]), OrderedDict(
    [('town', 'Berlin'), ('fips', '0900304300'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'East Berlin')]), OrderedDict(
    [('town', 'Berlin'), ('fips', '0900304300'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Kensington')]), OrderedDict(
    [('town', 'Bristol'), ('fips', '0900308490'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Forestville')]), OrderedDict(
    [('town', 'Canton'), ('fips', '0900312270'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Canton Center')]), OrderedDict(
    [('town', 'Canton'), ('fips', '0900312270'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Collinsville')]), OrderedDict(
    [('town', 'Canton'), ('fips', '0900312270'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'North Canton')]), OrderedDict(
    [('town', 'East Windsor'), ('fips', '0900324800'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Broad Brook')]), OrderedDict(
    [('town', 'East Windsor'), ('fips', '0900324800'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Melrose')]), OrderedDict(
    [('town', 'East Windsor'), ('fips', '0900324800'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Warehouse Point')]), OrderedDict(
    [('town', 'East Windsor'), ('fips', '0900324800'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Windsorville')]), OrderedDict(
    [('town', 'Enfield'), ('fips', '0900325990'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Hazardville')]), OrderedDict(
    [('town', 'Farmington'), ('fips', '0900327600'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Unionville')]), OrderedDict(
    [('town', 'Glastonbury'), ('fips', '0900331240'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'East Glastonbury')]), OrderedDict(
    [('town', 'Glastonbury'), ('fips', '0900331240'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'South Glastonbury')]), OrderedDict(
    [('town', 'Granby'), ('fips', '0900332640'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'North Granby')]), OrderedDict(
    [('town', 'Granby'), ('fips', '0900332640'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'West Granby')]), OrderedDict(
    [('town', 'Hartford'), ('fips', '0900337070'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Barry Square')]), OrderedDict(
    [('town', 'Hartford'), ('fips', '0900337070'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Blue Hills')]), OrderedDict(
    [('town', 'Hartford'), ('fips', '0900337070'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Central')]), OrderedDict(
    [('town', 'Hartford'), ('fips', '0900337070'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Unity Plaza')]), OrderedDict(
    [('town', 'Hartland'), ('fips', '0900337140'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'East  Hartland')]), OrderedDict(
    [('town', 'Hartland'), ('fips', '0900337140'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'West Hartland')]), OrderedDict(
    [('town', 'Manchester'), ('fips', '0900344700'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Buckland')]), OrderedDict(
    [('town', 'Simsbury'), ('fips', '0900368940'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Tariffville')]), OrderedDict(
    [('town', 'Simsbury'), ('fips', '0900368940'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Weatogue')]), OrderedDict(
    [('town', 'Simsbury'), ('fips', '0900368940'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'West Simsbury')]), OrderedDict(
    [('town', 'South Windsor'), ('fips', '0900371390'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Biseli')]), OrderedDict(
    [('town', 'South Windsor'), ('fips', '0900371390'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'East Windsor Hill')]), OrderedDict(
    [('town', 'Southington'), ('fips', '0900370550'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Marion')]), OrderedDict(
    [('town', 'Southington'), ('fips', '0900370550'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Milldale')]), OrderedDict(
    [('town', 'Southington'), ('fips', '0900370550'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Plantsville')]), OrderedDict(
    [('town', 'Suffield'), ('fips', '0900374540'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'West Suffield')]), OrderedDict(
    [('town', 'West Hartford'), ('fips', '0900382590'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', "Bishop''s Corner")]), OrderedDict(
    [('town', 'West Hartford'), ('fips', '0900382590'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Elmwood')]), OrderedDict(
    [('town', 'Windsor'), ('fips', '0900387000'), ('county_fips', '09003'), ('county', 'Hartford County'),
     ('subtown', 'Poquonock')]), OrderedDict(
    [('town', 'Barkhamsted'), ('fips', '0900502760'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Pleasant Valley')]), OrderedDict(
    [('town', 'Barkhamsted'), ('fips', '0900502760'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Riverton')]), OrderedDict(
    [('town', 'Canaan'), ('fips', '0900510940'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Falls Village')]), OrderedDict(
    [('town', 'Cornwall'), ('fips', '0900517240'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Cornwall Bridge')]), OrderedDict(
    [('town', 'Cornwall'), ('fips', '0900517240'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'West Cornwall')]), OrderedDict(
    [('town', 'Kent'), ('fips', '0900540290'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'South Kent')]), OrderedDict(
    [('town', 'Litchfield'), ('fips', '0900543370'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Bantam')]), OrderedDict(
    [('town', 'Litchfield'), ('fips', '0900543370'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Lyme Rock')]), OrderedDict(
    [('town', 'Litchfield'), ('fips', '0900543370'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Northfield')]), OrderedDict(
    [('town', 'Morris'), ('fips', '0900549460'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'East Morris')]), OrderedDict(
    [('town', 'Morris'), ('fips', '0900549460'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Lakeside')]), OrderedDict(
    [('town', 'New Hartford'), ('fips', '0900551350'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Bakersville')]), OrderedDict(
    [('town', 'New Hartford'), ('fips', '0900551350'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Pine Meadow')]), OrderedDict(
    [('town', 'New Milford'), ('fips', '0900552630'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Gaylordsville')]), OrderedDict(
    [('town', 'North Canaan'), ('fips', '0900554030'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Canaan')]), OrderedDict(
    [('town', 'North Canaan'), ('fips', '0900554030'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'East Canaan')]), OrderedDict(
    [('town', 'Plymouth'), ('fips', '0900560750'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Pequabuck')]), OrderedDict(
    [('town', 'Plymouth'), ('fips', '0900560750'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Terryville')]), OrderedDict(
    [('town', 'Salisbury'), ('fips', '0900566420'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Hotchkiss School')]), OrderedDict(
    [('town', 'Salisbury'), ('fips', '0900566420'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Lakeville')]), OrderedDict(
    [('town', 'Salisbury'), ('fips', '0900566420'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Taconic')]), OrderedDict(
    [('town', 'Washington'), ('fips', '0900579720'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Marble Dale')]), OrderedDict(
    [('town', 'Washington'), ('fips', '0900579720'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'New Preston')]), OrderedDict(
    [('town', 'Washington'), ('fips', '0900579720'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Washington Depot')]), OrderedDict(
    [('town', 'Watertown'), ('fips', '0900580490'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Oakville')]), OrderedDict(
    [('town', 'Winchester'), ('fips', '0900586440'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Winchester Center')]), OrderedDict(
    [('town', 'Winchester'), ('fips', '0900586440'), ('county_fips', '09005'), ('county', 'Litchfield County'),
     ('subtown', 'Winsted')]), OrderedDict(
    [('town', 'East Haddam'), ('fips', '0900722280'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Moodus')]), OrderedDict(
    [('town', 'East Hampton'), ('fips', '0900722490'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Cobalt')]), OrderedDict(
    [('town', 'East Hampton'), ('fips', '0900722490'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Middle Haddam')]), OrderedDict(
    [('town', 'Essex'), ('fips', '0900726270'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Centerbrook')]), OrderedDict(
    [('town', 'Essex'), ('fips', '0900726270'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Ivoryton')]), OrderedDict(
    [('town', 'Haddam'), ('fips', '0900735230'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Higganum')]), OrderedDict(
    [('town', 'Middlefield'), ('fips', '0900747080'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Rockfall')]), OrderedDict(
    [('town', 'Middletown'), ('fips', '0900747360'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Baileyville')]), OrderedDict(
    [('town', 'Middletown'), ('fips', '0900747360'), ('county_fips', '09007'), ('county', 'Middlesex County'),
     ('subtown', 'Wesleyan')]), OrderedDict(
    [('town', 'Branford'), ('fips', '0900907310'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Short Beach')]), OrderedDict(
    [('town', 'Branford'), ('fips', '0900907310'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Stony Creek')]), OrderedDict(
    [('town', 'Derby'), ('fips', '0900919550'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'East Derby')]), OrderedDict(
    [('town', 'Hamden'), ('fips', '0900935650'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Centerville')]), OrderedDict(
    [('town', 'Hamden'), ('fips', '0900935650'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Mt Carmel')]), OrderedDict(
    [('town', 'Hamden'), ('fips', '0900935650'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Whitneyville')]), OrderedDict(
    [('town', 'Meriden'), ('fips', '0900946520'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'South Meriden')]), OrderedDict(
    [('town', 'Milford'), ('fips', '0900947535'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Devon')]), OrderedDict(
    [('town', 'Milford'), ('fips', '0900947535'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Wildermere Beach')]), OrderedDict(
    [('town', 'Milford'), ('fips', '0900947535'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Woodmont')]), OrderedDict(
    [('town', 'Naugatuck'), ('fips', '0900949950'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Union City')]), OrderedDict(
    [('town', 'New Haven'), ('fips', '0900952070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Amity')]), OrderedDict(
    [('town', 'New Haven'), ('fips', '0900952070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Fair Haven')]), OrderedDict(
    [('town', 'New Haven'), ('fips', '0900952070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Terminal')]), OrderedDict(
    [('town', 'New Haven'), ('fips', '0900952070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Westville')]), OrderedDict(
    [('town', 'New Haven'), ('fips', '0900952070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Yale')]), OrderedDict(
    [('town', 'North Branford'), ('fips', '0900953890'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Northford')]), OrderedDict(
    [('town', 'Southbury'), ('fips', '0900969640'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'South Britain')]), OrderedDict(
    [('town', 'Wallingford'), ('fips', '0900978740'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Gayesville')]), OrderedDict(
    [('town', 'Wallingford'), ('fips', '0900978740'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Yalesville')]), OrderedDict(
    [('town', 'Waterbury'), ('fips', '0900980070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'East End')]), OrderedDict(
    [('town', 'Waterbury'), ('fips', '0900980070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'North End')]), OrderedDict(
    [('town', 'Waterbury'), ('fips', '0900980070'), ('county_fips', '09009'), ('county', 'New Haven County'),
     ('subtown', 'Waterville')]), OrderedDict(
    [('town', 'Bozrah'), ('fips', '0901106820'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Fitchville')]), OrderedDict(
    [('town', 'Bozrah'), ('fips', '0901106820'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Gilman')]), OrderedDict(
    [('town', 'Colchester'), ('fips', '0901115910'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'North Westchester')]), OrderedDict(
    [('town', 'East Lyme'), ('fips', '0901123400'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Niantic')]), OrderedDict(
    [('town', 'Franklin'), ('fips', '0901129910'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'North Franklin')]), OrderedDict(
    [('town', 'Griswold'), ('fips', '0901133900'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Glasgo')]), OrderedDict(
    [('town', 'Griswold'), ('fips', '0901133900'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Jewett City')]), OrderedDict(
    [('town', 'Groton'), ('fips', '0901134250'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Groton City')]), OrderedDict(
    [('town', 'Groton'), ('fips', '0901134250'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Groton Long Point')]), OrderedDict(
    [('town', 'Groton'), ('fips', '0901134250'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Noank')]), OrderedDict(
    [('town', 'Groton'), ('fips', '0901134250'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Submarine Base')]), OrderedDict(
    [('town', 'Groton'), ('fips', '0901134250'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'West Mystic')]), OrderedDict(
    [('town', 'Ledyard'), ('fips', '0901142600'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Gales Ferry')]), OrderedDict(
    [('town', 'Lyme'), ('fips', '0901144210'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Hadlyme')]), OrderedDict(
    [('town', 'Montville'), ('fips', '0901148900'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Oakdale')]), OrderedDict(
    [('town', 'Montville'), ('fips', '0901148900'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Uncasville')]), OrderedDict(
    [('town', 'New London'), ('fips', '0901152350'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Coast Guard Acad')]), OrderedDict(
    [('town', 'New London'), ('fips', '0901152350'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Conn College')]), OrderedDict(
    [('town', 'Norwich'), ('fips', '0901156270'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Taftville')]), OrderedDict(
    [('town', 'Norwich'), ('fips', '0901156270'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Yantic')]), OrderedDict(
    [('town', 'Old Lyme'), ('fips', '0901157040'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'South Lyme')]), OrderedDict(
    [('town', 'Preston'), ('fips', '0901162150'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Poquetanuck')]), OrderedDict(
    [('town', 'Sprague'), ('fips', '0901171670'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Baltic')]), OrderedDict(
    [('town', 'Sprague'), ('fips', '0901171670'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Hanover')]), OrderedDict(
    [('town', 'Sprague'), ('fips', '0901171670'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Versailles')]), OrderedDict(
    [('town', 'Stonington'), ('fips', '0901173770'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Mystic')]), OrderedDict(
    [('town', 'Stonington'), ('fips', '0901173770'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Old Mystic')]), OrderedDict(
    [('town', 'Stonington'), ('fips', '0901173770'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Pawcatuck')]), OrderedDict(
    [('town', 'Stonington'), ('fips', '0901173770'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Wequetequock')]), OrderedDict(
    [('town', 'Waterford'), ('fips', '0901180280'), ('county_fips', '09011'), ('county', 'New London County'),
     ('subtown', 'Quaker Hill')]), OrderedDict(
    [('town', 'Hebron'), ('fips', '0901337910'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Amston')]), OrderedDict(
    [('town', 'Mansfield'), ('fips', '0901344910'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Mansfield Center')]), OrderedDict(
    [('town', 'Mansfield'), ('fips', '0901344910'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Mansfield Depot')]), OrderedDict(
    [('town', 'Mansfield'), ('fips', '0901344910'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Merrow')]), OrderedDict(
    [('town', 'Mansfield'), ('fips', '0901344910'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Storrs')]), OrderedDict(
    [('town', 'Somers'), ('fips', '0901369220'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Somersville')]), OrderedDict(
    [('town', 'Stafford'), ('fips', '0901372090'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Stafford Springs')]), OrderedDict(
    [('town', 'Stafford'), ('fips', '0901372090'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Staffordville')]), OrderedDict(
    [('town', 'Vernon'), ('fips', '0901378250'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Rockville')]), OrderedDict(
    [('town', 'Vernon'), ('fips', '0901378250'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'Talcottville')]), OrderedDict(
    [('town', 'Willington'), ('fips', '0901385950'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'South Willington')]), OrderedDict(
    [('town', 'Willington'), ('fips', '0901385950'), ('county_fips', '09013'), ('county', 'Tolland County'),
     ('subtown', 'West Willington')]), OrderedDict(
    [('town', 'Ashford'), ('fips', '0901501430'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Warrenville')]), OrderedDict(
    [('town', 'Killingly'), ('fips', '0901540500'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Ballouville')]), OrderedDict(
    [('town', 'Killingly'), ('fips', '0901540500'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Danielson')]), OrderedDict(
    [('town', 'Killingly'), ('fips', '0901540500'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Dayville')]), OrderedDict(
    [('town', 'Killingly'), ('fips', '0901540500'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'East Killingly')]), OrderedDict(
    [('town', 'Killingly'), ('fips', '0901540500'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Rogers')]), OrderedDict(
    [('town', 'Killingly'), ('fips', '0901540500'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'South Killingly')]), OrderedDict(
    [('town', 'Plainfield'), ('fips', '0901559980'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Central Village')]), OrderedDict(
    [('town', 'Plainfield'), ('fips', '0901559980'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Moosup')]), OrderedDict(
    [('town', 'Plainfield'), ('fips', '0901559980'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Wauregan')]), OrderedDict(
    [('town', 'Pomfret'), ('fips', '0901561030'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Abington')]), OrderedDict(
    [('town', 'Pomfret'), ('fips', '0901561030'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Pomfret Center')]), OrderedDict(
    [('town', 'Putnam'), ('fips', '0901562710'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'East Putnam')]), OrderedDict(
    [('town', 'Sterling'), ('fips', '0901573420'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Oneco')]), OrderedDict(
    [('town', 'Thompson'), ('fips', '0901575870'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Fabyan')]), OrderedDict(
    [('town', 'Thompson'), ('fips', '0901575870'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Grosvenor Dale')]), OrderedDict(
    [('town', 'Thompson'), ('fips', '0901575870'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Mechanicsville')]), OrderedDict(
    [('town', 'Thompson'), ('fips', '0901575870'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'n. Grosvenordale')]), OrderedDict(
    [('town', 'Thompson'), ('fips', '0901575870'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'North Grosvenor Dale')]), OrderedDict(
    [('town', 'Thompson'), ('fips', '0901575870'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Quinebaug')]), OrderedDict(
    [('town', 'Windham'), ('fips', '0901586790'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'North Windham')]), OrderedDict(
    [('town', 'Windham'), ('fips', '0901586790'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'South Windham')]), OrderedDict(
    [('town', 'Windham'), ('fips', '0901586790'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Willimantic')]), OrderedDict(
    [('town', 'Woodstock'), ('fips', '0901588190'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'East Woodstock')]), OrderedDict(
    [('town', 'Woodstock'), ('fips', '0901588190'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'North Woodstock')]), OrderedDict(
    [('town', 'Woodstock'), ('fips', '0901588190'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'South Woodstock')]), OrderedDict(
    [('town', 'Woodstock'), ('fips', '0901588190'), ('county_fips', '09015'), ('county', 'Windham County'),
     ('subtown', 'Woodstock Valley')])]
