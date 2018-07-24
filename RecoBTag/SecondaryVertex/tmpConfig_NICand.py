import FWCore.ParameterSet.Config as cms

process = cms.Process("DATA")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:////pnfs/desy.de/cms/tier2/store/data/Run2017A/SingleMuon/AOD/PromptReco-v2/000/296/168/00000/9AF5B3F6-444C-E711-B5C7-02163E013729.root'),
    lumisToProcess = cms.untracked.VLuminosityBlockRange( (
        "297050:12-297050:137", "297050:193-297050:776", "297056:12-297056:203", "297057:1-297057:4", "297057:14-297057:105", 
        "297057:112-297057:377", "297057:385-297057:418", "297057:424-297057:509", "297057:516-297057:906", "297099:24-297099:62", 
        "297100:1-297100:15", "297100:21-297100:369", "297100:375-297100:381", "297101:1-297101:668", "297101:673-297101:697", 
        "297101:700-297101:856", "297101:862-297101:937", "297101:943-297101:1101", "297113:1-297113:204", "297113:211-297113:252", 
        "297114:1-297114:99", "297114:106-297114:161", "297175:1-297175:85", "297176:11-297176:120", "297176:125-297176:214", 
        "297177:1-297177:162", "297178:1-297178:54", "297178:59-297178:334", "297178:342-297178:749", "297178:754-297178:967", 
        "297178:972-297178:1037", "297178:1043-297178:1264", "297178:1272-297178:1282", "297178:1290-297178:1385", "297215:1-297215:47", 
        "297218:1-297218:27", "297219:1-297219:80", "297219:85-297219:281", "297219:288-297219:579", "297219:585-297219:916", 
        "297219:921-297219:1429", "297219:1436-297219:2004", "297219:2010-297219:2638", "297224:10-297224:19", "297224:24-297224:138", 
        "297225:1-297225:32", "297227:9-297227:192", "297292:1-297292:125", "297292:130-297292:131", "297292:136-297292:667", 
        "297292:675-297292:753", "297293:1-297293:121", "297293:127-297293:150", "297296:1-297296:236", "297296:240-297296:401", 
        "297296:406-297296:418", "297296:425-297296:497", "297308:1-297308:44", "297359:39-297359:70", "297359:164-297359:180", 
        "297411:32-297411:737", "297411:740-297411:800", "297411:807-297411:950", "297424:32-297424:149", "297425:1-297425:107", 
        "297425:112-297425:157", "297426:1-297426:28", "297426:34-297426:84", "297426:90-297426:111", "297429:1-297429:72", 
        "297430:1-297430:199", "297431:1-297431:49", "297431:55-297431:64", "297431:71-297431:188", "297432:1-297432:112", 
        "297433:1-297433:159", "297434:1-297434:161", "297435:1-297435:94", "297467:50-297467:138", "297468:1-297468:74", 
        "297469:1-297469:4", "297469:9-297469:70", "297483:37-297483:68", "297483:71-297483:201", "297483:206-297483:214", 
        "297484:1-297484:47", "297484:53-297484:208", "297484:214", "297485:1-297485:16", "297485:23-297485:253", 
        "297485:258-297485:299", "297485:302-297485:314", "297485:321-297485:420", "297486:1-297486:74", "297486:79-297486:598", 
        "297486:603-297486:625", "297487:1-297487:433", "297487:439-297487:491", "297487:495-297487:603", "297487:609-297487:613", 
        "297488:1-297488:73", "297488:80-297488:424", "297503:5-297503:275", "297503:282-297503:559", "297503:566-297503:606", 
        "297503:612-297503:635", "297503:642-297503:772", "297503:777-297503:779", "297504:1-297504:41", "297504:125-297504:136", 
        "297505:1-297505:394", "297557:8-297557:28", "297557:67-297557:113", "297557:119-297557:167", "297557:173-297557:174", 
        "297557:180-297557:394", "297558:9-297558:266", "297562:1-297562:69", "297562:120-297562:369", "297563:1-297563:254", 
        "297563:260-297563:264", "297598:17", "297598:22-297598:33", "297599:1-297599:169", "297599:211-297599:225", 
        "297599:230-297599:312", "297599:319-297599:385", "297599:395-297599:407", "297603:1-297603:420", "297604:1-297604:126", 
        "297604:131-297604:272", "297604:279-297604:375", "297604:381-297604:407", "297605:1-297605:6", "297605:13-297605:20", 
        "297605:24-297605:89", "297605:95-297605:223", "297605:257-297605:407", "297606:1-297606:94", "297606:99-297606:231", 
        "297620:32-297620:318", "297656:64-297656:116", "297656:123-297656:135", "297656:140-297656:230", "297656:269-297656:307", 
        "297656:313-297656:330", "297656:341-297656:388", "297656:393-297656:433", "297665:1-297665:153", "297665:159-297665:209", 
        "297665:214-297665:279", "297666:1-297666:11", "297666:17-297666:81", "297666:86-297666:121", "297670:21-297670:34", 
        "297674:3-297674:102", "297674:108-297674:188", "297675:1-297675:123", "297675:129-297675:239", "297675:244-297675:328", 
        "297675:334-297675:467", "297675:470-297675:471", "297722:55-297722:160", "297722:165-297722:353", "297723:1-297723:13", 
        "297723:51-297723:222", "298996:33-298996:216", "298997:1-298997:37", "298997:47", "299000:4-299000:77", 
        "299042:33-299042:55", "299061:38-299061:355", "299062:1-299062:163", "299062:166-299062:303", "299064:7-299064:85", 
        "299065:13-299065:248", "299065:251-299065:342", "299067:1-299067:459", "299096:2-299096:97", "299149:29-299149:470", 
        "299178:37-299178:56", "299178:58-299178:111", "299180:5-299180:98", "299184:1-299184:561", "299185:1-299185:120", 
        "299327:1-299327:72", "299329:1-299329:172", "299368:37-299368:175", "299369:1-299369:303", "299370:1-299370:7", 
        "299370:47-299370:705", "299380:34-299380:227", "299381:1-299381:45", "299394:5-299394:33", "299395:1-299395:187", 
        "299396:1-299396:81", "299420:2-299420:50", "299443:145-299443:164", "299450:39-299450:88", "299477:39-299477:42", 
        "299477:82-299477:87", "299478:1-299478:175", "299479:1-299479:123", "299480:1-299480:715", "299481:1-299481:196", 
        "299481:199-299481:236", "299481:260-299481:479", "299481:487-299481:940", "299481:943-299481:1037", "299481:1061-299481:1257", 
        "299593:95-299593:177", "299593:179-299593:896", "299594:1-299594:317", "299595:1-299595:134", "299595:138", 
        "299597:3-299597:91", "299597:93-299597:540", "299649:151-299649:332", "300087:36-300087:59", "300087:61-300087:126", 
        "300087:128-300087:216", "300087:218-300087:239", "300105:1-300105:21", "300106:1-300106:74", "300107:1-300107:28", 
        "300107:30-300107:47", "300117:35-300117:67", "300122:46-300122:730", "300122:735-300122:924", "300122:927-300122:1295", 
        "300123:1-300123:384", "300123:387-300123:612", "300155:35-300155:1229", "300156:1-300156:72", "300157:9-300157:1107", 
        "300226:43-300226:448", "300233:43-300233:162", "300234:1-300234:59", "300235:1-300235:187", "300236:11-300236:187", 
        "300237:1-300237:713", "300237:716-300237:717", "300238:30-300238:58", "300238:62-300238:329", "300239:1-300239:145", 
        "300239:148-300239:167", "300239:171-300239:213", "300240:1-300240:7", "300240:11-300240:46", "300240:51-300240:362", 
        "300280:52-300280:56", "300280:61-300280:69", "300280:73-300280:150", "300280:155-300280:165", "300280:178-300280:198", 
        "300280:207-300280:222", "300280:226-300280:251", "300280:255-300280:268", "300280:275-300280:345", "300280:349-300280:370", 
        "300280:381-300280:548", "300280:553-300280:607", "300280:617-300280:639", "300280:663-300280:691", "300281:3-300281:8", 
        "300282:1-300282:9", "300282:13-300282:59", "300282:73-300282:92", "300282:97-300282:114", "300282:142-300282:151", 
        "300282:156-300282:186", "300283:1-300283:34", "300284:1-300284:22", "300284:38-300284:47", "300284:50-300284:82", 
        "300284:90-300284:98", "300284:108-300284:130", "300284:133-300284:152", "300284:156-300284:250", "300284:260-300284:414", 
        "300284:420-300284:561", "300284:568-300284:585", "300284:590-300284:680", "300284:691-300284:751", "300364:27-300364:46", 
        "300365:1-300365:20", "300366:1-300366:21", "300367:1-300367:20", "300368:1-300368:20", "300369:1-300369:20", 
        "300370:1-300370:20", "300371:1-300371:20", "300372:1-300372:8", "300373:1-300373:21", "300374:1-300374:21", 
        "300375:1-300375:93", "300389:1", "300389:4-300389:5", "300389:8", "300389:11-300389:20", 
        "300389:23-300389:39", "300389:60-300389:149", "300390:2-300390:21", "300391:1-300391:21", "300392:1-300392:21", 
        "300393:1-300393:20", "300394:1-300394:21", "300395:1-300395:20", "300396:1-300396:20", "300397:1-300397:20", 
        "300398:1-300398:20", "300399:1-300399:20", "300400:1-300400:677", "300401:19-300401:673", "300459:40-300459:332", 
        "300461:1-300461:98", "300462:1-300462:97", "300463:1-300463:124", "300464:1-300464:103", "300464:126-300464:265", 
        "300466:1-300466:650", "300467:1-300467:563", "300497:26-300497:175", "300514:38-300514:150", "300515:1-300515:838", 
        "300515:957-300515:1013", "300516:1-300516:111", "300517:1-300517:8", "300517:103-300517:623", "300558:8-300558:548", 
        "300560:1-300560:640", "300560:645-300560:844", "300574:15-300574:111", "300575:1-300575:82", "300576:7-300576:123", 
        "300576:125-300576:1206", "300631:41-300631:49", "300631:63-300631:66", "300631:75-300631:226", "300632:1-300632:21", 
        "300633:1-300633:447", "300635:1-300635:23", "300635:26-300635:176", "300636:1-300636:335", "300636:338-300636:1572", 
        "300673:41-300673:47", "300673:49", "300673:52-300673:56", "300673:59-300673:66", "300674:1-300674:33", 
        "300675:1-300675:33", "300676:1-300676:26", "300742:56-300742:343", "300777:21-300777:509", "300780:3-300780:341", 
        "300785:1-300785:549", "300785:552-300785:750", "300785:752-300785:1201", "300785:1219-300785:1272", "300806:36-300806:214", 
        "300811:6-300811:508", "300812:1-300812:59", "300816:6-300816:161", "300817:1-300817:33", "300817:36-300817:74", 
        "300817:80-300817:383", "300817:410-300817:493", "301046:162-301046:223", "301141:25-301141:31", "301142:1-301142:897", 
        "301161:36-301161:805", "301165:1-301165:145", "301179:35-301179:59", "301180:1-301180:97", "301183:3-301183:10", 
        "301183:13-301183:303", "301281:38-301281:157", "301283:3-301283:886", "301298:45-301298:949", "301323:35-301323:474", 
        "301323:477-301323:990", "301330:22-301330:353", "301359:33-301359:319", "301384:1-301384:476", "301391:38-301391:214", 
        "301392:1-301392:627", "301393:2-301393:18", "301396:1-301396:33", "301397:1-301397:228", "301397:231-301397:728", 
        "301398:1-301398:9", "301399:1-301399:108", "301417:50-301417:367", "301447:86-301447:96", "301447:99-301447:400", 
        "301447:404-301447:512", "301448:1-301448:329", "301449:1-301449:404", "301450:1-301450:173", "301461:28-301461:581", 
        "301472:35-301472:830", "301475:1-301475:18", "301476:1-301476:844", "301519:42-301519:250", "301524:1-301524:110", 
        "301524:117-301524:263", "301529:1-301529:49", "301530:1-301530:110", "301531:1-301531:394", "301532:1-301532:611", 
        "301567:14-301567:372", "301627:57-301627:943", "301664:28-301664:445", "301665:1-301665:294", "301665:319-301665:487", 
        "301694:36-301694:102", "301912:43-301912:52", "301912:101-301912:422", "301913:1-301913:58", "301914:1-301914:350", 
        "301941:31-301941:568", "301959:30-301959:1938", "301960:1-301960:147", "301970:6-301970:123", "301984:17-301984:317", 
        "301985:1-301985:367", "301986:1-301986:381", "301987:1-301987:1128", "301997:37-301997:407", "301998:1-301998:1704", 
        "302019:34-302019:86", "302026:24-302026:53", "302026:66-302026:72", "302029:1-302029:98", "302031:1-302031:401", 
        "302031:403-302031:446", "302031:448-302031:675", "302031:678-302031:818", "302033:1-302033:40", "302033:44-302033:46", 
        "302034:1-302034:20", "302037:18-302037:20", "302038:10", "302040:1-302040:174", "302041:1-302041:72", 
        "302042:1-302042:523", "302043:1-302043:228", "302131:71-302131:943", "302159:33-302159:140", "302163:32-302163:671", 
        "302163:674-302163:1230", "302165:1-302165:85", "302166:1-302166:16", "302225:54-302225:133", "302225:136-302225:923", 
        "302228:58-302228:78", "302228:81-302228:293", "302229:1-302229:457", "302240:1-302240:960", "302262:37-302262:471", 
        "302263:1-302263:1250", "302277:15-302277:17", "302277:22-302277:192", "302277:194-302277:391", "302279:1-302279:71", 
        "302280:1-302280:152", "302322:33-302322:870", "302328:42-302328:722", "302337:27-302337:162", "302342:19-302342:72", 
        "302343:1-302343:98", "302344:3-302344:482", "302350:1-302350:136", "302388:27-302388:157", "302388:164-302388:717", 
        "302392:45-302392:407", "302393:1-302393:887", "302448:21-302448:312", "302448:317-302448:442", "302448:445-302448:483", 
        "302448:486-302448:1926", "302472:28-302472:808", "302473:1-302473:368", "302473:398-302473:406", "302474:1-302474:305", 
        "302475:1-302475:7", "302476:1-302476:259", "302479:30-302479:222", "302479:225-302479:340", "302484:8-302484:176", 
        "302485:1-302485:922", "302492:10-302492:21", "302492:23-302492:59", "302493:1-302493:7", "302494:1-302494:618", 
        "302509:73-302509:92", "302513:37-302513:89", "302522:29-302522:46", "302523:1-302523:59", "302525:1-302525:677", 
        "302525:747-302525:778", "302526:1-302526:582", "302548:40-302548:124", "302551:1-302551:7", "302553:1-302553:188", 
        "302554:1-302554:7", "302555:1-302555:11", "302563:40-302563:46", "302565:1-302565:7", "302572:6-302572:291", 
        "302573:1-302573:693", "302573:730-302573:1285", "302596:47-302596:534", "302596:545-302596:705", "302596:710-302596:986", 
        "302597:1-302597:1054", "302634:37-302634:73", "302634:75-302634:123", "302634:125-302634:129", "302634:133-302634:165", 
        "302634:168-302634:175", "302634:177-302634:216", "302634:218-302634:358", "302634:361-302634:375", "302634:378-302634:404", 
        "302634:407-302634:423", "302634:425-302634:503", "302634:505-302634:578", "302634:581-302634:594", "302634:596-302634:638", 
        "302635:1-302635:22", "302635:24-302635:28", "302635:30-302635:39", "302635:41-302635:53", "302635:55-302635:132", 
        "302635:134-302635:144", "302635:146-302635:265", "302635:267-302635:271", "302635:274-302635:344", "302635:347-302635:357", 
        "302635:359-302635:375", "302635:378-302635:384", "302635:386-302635:414", "302635:416-302635:494", "302635:497-302635:608", 
        "302635:611-302635:634", "302635:637-302635:684", "302635:687-302635:706", "302635:708-302635:724", "302635:726-302635:901", 
        "302635:904-302635:954", "302635:957-302635:982", "302635:984-302635:1072", "302635:1075-302635:1124", "302635:1126-302635:1129", 
        "302635:1132-302635:1206", "302635:1209-302635:1234", "302635:1236-302635:1291", "302651:1-302651:149", "302654:1-302654:317", 
        "302661:1-302661:72", "302663:1-302663:706", "303825:1-303825:180", "303832:54-303832:1334", "303832:1338-303832:1913", 
        "303838:54", "303838:83-303838:2044", "303885:60-303885:2052", "303948:55-303948:1678", "303998:58-303998:319", 
        "303999:1-303999:751", "304000:1-304000:56", "304062:54-304062:2014", "304119:71-304119:138", "304119:143-304119:150", 
        "304120:1-304120:253", "304125:1-304125:1769", "304144:76-304144:2596", "304144:2598-304144:2656", "304158:165-304158:1750", 
        "304158:1752-304158:2087", "304169:50-304169:1714", "304169:1731-304169:1733", "304170:1-304170:620", "304199:10-304199:18", 
        "304200:1-304200:321", "304204:55-304204:607", "304209:52-304209:98", "304209:100-304209:133", "304209:135-304209:157", 
        "304209:176-304209:253", "304209:255-304209:477", "304291:56-304291:85", "304292:1-304292:1125", "304292:1183-304292:1779", 
        "304292:1781-304292:1811", "304333:74-304333:1653", "304354:82-304354:295", "304366:44-304366:1387", "304366:1390-304366:1396", 
        "304366:1399-304366:1402", "304366:1404-304366:1407", "304366:1409-304366:1412", "304366:1414-304366:1416", "304366:1419-304366:1421", 
        "304366:1424-304366:1873", "304446:40-304446:92", "304446:110-304446:111", "304447:1-304447:534", "304447:540-304447:1644", 
        "304451:1-304451:60", "304505:60-304505:86", "304506:1-304506:370", "304507:1-304507:239", "304508:1-304508:1324", 
        "304562:52-304562:56", "304562:60-304562:848", "304616:52-304616:223", "304616:227-304616:740", "304616:747-304616:1002", 
        "304625:73-304625:536", "304626:1-304626:8", "304654:53-304654:704", "304655:1-304655:1194", "304661:53-304661:67", 
        "304661:69-304661:143", "304661:147-304661:173", "304661:175-304661:198", "304661:237-304661:240", "304662:1-304662:150", 
        "304663:1-304663:689", "304671:51-304671:1193", "304672:1-304672:60", "304737:69-304737:149", "304738:1-304738:1681", 
        "304739:3-304739:16", "304740:1-304740:278", "304776:49-304776:98", "304777:1-304777:431", "304777:438-304777:510", 
        "304778:4-304778:1300", "304797:28-304797:87", "304797:91-304797:306", "304797:308-304797:377", "304797:385-304797:1202", 
        "304797:1205-304797:2950", "305044:3-305044:203", "305044:302-305044:306", "305044:309-305044:310", "305044:313", 
        "305044:318-305044:330", "305045:1-305045:873", "305046:1-305046:667", "305046:671-305046:686", "305059:63-305059:518", 
        "305059:520-305059:575", "305062:1-305062:8", "305063:1-305063:35", "305064:1-305064:2045", "305081:52-305081:1107", 
        "305112:68-305112:1527", "305113:9-305113:72", "305114:1-305114:526", "305178:69-305178:124", "305179:1-305179:21", 
        "305180:1-305180:9", "305181:1-305181:8", "305182:1-305182:8", "305183:1-305183:231", "305183:262-305183:266", 
        "305184:1-305184:8", "305186:1-305186:112", "305186:120-305186:422", "305188:1-305188:1002", "305202:74-305202:132", 
        "305202:136-305202:729", "305204:1-305204:1229", "305207:52-305207:1077", "305208:1-305208:372", "305234:52-305234:99", 
        "305236:1-305236:23", "305237:1-305237:16", "305237:18-305237:1147", "305247:57-305247:433", "305248:1-305248:957", 
        "305252:1-305252:548", "305282:75-305282:207", "305310:60-305310:157", "305310:163-305310:458", "305311:1-305311:153", 
        "305312:1-305312:227", "305313:1-305313:741", "305314:1-305314:404", "305336:36-305336:241", "305338:1-305338:107", 
        "305341:1-305341:503", "305349:1-305349:34", "305350:1-305350:21", "305351:1-305351:868", "305358:91-305358:231", 
        "305358:233-305358:253", "305364:50-305364:147", "305365:1-305365:668", "305365:676-305365:832", "305366:1-305366:721", 
        "305366:724-305366:756", "305366:769-305366:1254", "305376:71-305376:168", "305377:9-305377:1292", "305377:1294-305377:1383", 
        "305377:1386-305377:1525", "305405:44-305405:536", "305405:573-305405:575", "305406:1-305406:394", "305406:401-305406:520", 
        "305406:528-305406:535", "305406:540-305406:1475", "305440:20-305440:291", "305441:1-305441:121", "305516:46-305516:518", 
        "305516:558-305516:639", "305517:1-305517:163", "305518:1-305518:1134", "305586:53-305586:583", "305589:1-305589:691", 
        "305590:1-305590:500", "305590:517-305590:1020", "305636:60-305636:339", "305636:342-305636:667", "305636:671-305636:2390", 
        "305766:55-305766:902", "305809:56-305809:197", "305814:85-305814:689", "305814:692-305814:978", "305814:980-305814:1074", 
        "305814:1077-305814:1912", "305821:59-305821:830", "305832:87-305832:266", "305840:1-305840:1144", "305842:1-305842:862", 
        "305862:81-305862:705", "305898:70-305898:780", "305902:53-305902:521", "305967:1-305967:32", "306029:63-306029:96", 
        "306030:1-306030:110", "306036:60-306036:63", "306037:1-306037:49", "306038:1-306038:139", "306041:1-306041:320", 
        "306042:1-306042:371", "306048:1-306048:140", "306049:1-306049:358", "306051:1-306051:415", "306091:422-306091:629", 
        "306092:1-306092:588", "306092:593-306092:976", "306095:1-306095:300", "306121:57-306121:152", "306122:1-306122:127", 
        "306125:1-306125:756", "306125:770-306125:2642", "306125:2667-306125:3007", "306126:1-306126:497", "306134:53-306134:84", 
        "306135:1-306135:1095", "306138:1-306138:1298", "306139:1-306139:1112", "306153:78-306153:165", "306154:1-306154:251", 
        "306154:253-306154:691", "306154:709-306154:1233", "306155:1-306155:1440", "306169:1-306169:745", "306170:1-306170:22", 
        "306171:1-306171:503", "306418:1-306418:33", "306418:35-306418:75", "306419:1-306419:62", "306420:1-306420:108", 
        "306422:9-306422:126", "306423:1-306423:333", "306432:1-306432:339", "306454:13-306454:101", "306455:1-306455:11", 
        "306456:1-306456:237", "306456:239-306456:787", "306457:1-306457:31", "306458:1-306458:17", "306458:20-306458:35", 
        "306458:37-306458:41", "306458:43-306458:47", "306458:49-306458:53", "306458:56-306458:60", "306458:62-306458:66", 
        "306458:68-306458:72", "306458:74-306458:77", "306458:79-306458:83", "306458:85-306458:89", "306458:93-306458:102", 
        "306458:104-306458:108", "306458:110-306458:114", "306458:116-306458:120", "306458:122-306458:126", "306458:129-306458:139", 
        "306458:141-306458:145", "306458:147-306458:151", "306458:153-306458:166", "306458:169-306458:173", "306458:175-306458:179", 
        "306458:181-306458:185", "306458:187-306458:191", "306458:193-306458:197", "306458:200-306458:210", "306458:212-306458:216", 
        "306458:218-306458:222", "306458:225-306458:229", "306458:231-306458:235", "306458:237-306458:241", "306458:243-306458:247", 
        "306458:249", "306458:252-306458:256", "306458:258-306458:268", "306459:1-306459:512", "306459:514-306459:2275", 
        "306460:1-306460:73"
     ) )
)
process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.candidateVertexArbitrator = cms.EDProducer("CandidateVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("candidateVertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("particleFlow")
)


process.candidateVertexArbitrator0 = cms.EDProducer("CandidateVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("candidateVertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("vertexAndTracksCandCleaned0")
)


process.candidateVertexArbitratorCvsL = cms.EDProducer("CandidateVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("candidateVertexMergerCvsL"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("particleFlow")
)


process.candidateVertexArbitratorDefault = cms.EDProducer("CandidateVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("candidateVertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("particleFlow")
)


process.candidateVertexMerger = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveCandidateVertexFinder")
)


process.candidateVertexMerger0 = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveCandidateVertexFinder0")
)


process.candidateVertexMergerCvsL = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveCandidateVertexFinderCvsL")
)


process.inclusiveCandidateSecondaryVertices = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("candidateVertexArbitrator")
)


process.inclusiveCandidateSecondaryVerticesCvsL = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("candidateVertexArbitratorCvsL")
)


process.inclusiveCandidateVertexFinder = cms.EDProducer("InclusiveCandidateVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        maxTimeSignificance = cms.double(3.5),
        seedMax3DIPSignificance = cms.double(9999),
        seedMax3DIPValue = cms.double(9999),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minHits = cms.uint32(0),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("particleFlow"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveCandidateVertexFinder0 = cms.EDProducer("InclusiveCandidateVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        maxTimeSignificance = cms.double(3.5),
        seedMax3DIPSignificance = cms.double(9999),
        seedMax3DIPValue = cms.double(9999),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minHits = cms.uint32(0),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("vertexAndTracksCandCleaned0"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveCandidateVertexFinderCvsL = cms.EDProducer("InclusiveCandidateVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        maxTimeSignificance = cms.double(3.5),
        seedMax3DIPSignificance = cms.double(9999),
        seedMax3DIPValue = cms.double(9999),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minHits = cms.uint32(0),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("particleFlow"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(1.25),
    vertexMinDLenSig = cms.double(0.25),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveCandidateVertexFinderDefault = cms.EDProducer("InclusiveCandidateVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        maxTimeSignificance = cms.double(3.5),
        seedMax3DIPSignificance = cms.double(9999),
        seedMax3DIPValue = cms.double(9999),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minHits = cms.uint32(0),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("particleFlow"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveSecondaryVertices = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("trackVertexArbitrator")
)


process.inclusiveSecondaryVertices0 = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("candidateVertexArbitrator0")
)


process.inclusiveSecondaryVerticesCleaned0 = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("candidateVertexArbitrator0")
)


process.inclusiveVertexFinder = cms.EDProducer("InclusiveVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        maxTimeSignificance = cms.double(3.5),
        seedMax3DIPSignificance = cms.double(9999),
        seedMax3DIPValue = cms.double(9999),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveVertexFinderDefault = cms.EDProducer("InclusiveVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        maxTimeSignificance = cms.double(3.5),
        seedMax3DIPSignificance = cms.double(9999),
        seedMax3DIPValue = cms.double(9999),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.nuclearInteractionIdentifier0 = cms.EDProducer("NuclearInteractionCandidateIdentifier",
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    selection = cms.PSet(
        position = cms.vdouble(
            2.17, 2.25, 2.694, 3.481, 6.597, 
            7.278, 10.7, 11.344, 15.797, 16.43
        )
    )
)


process.nuclearInteractionIdentifierAfterRefit = cms.EDProducer("NuclearInteractionCandidateIdentifier",
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("vertexRefitted0"),
    selection = cms.PSet(
        position = cms.vdouble(
            2.17, 2.25, 2.694, 3.481, 6.597, 
            7.278, 10.7, 11.344, 15.797, 16.43
        )
    )
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.trackVertexArbitrator = cms.EDProducer("TrackVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("vertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.trackVertexArbitratorDefault = cms.EDProducer("TrackVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("vertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.vertexAndTracksCandCleaned = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("particleFlow"),
    veto = cms.InputTag("nuclearInteractionCandIdentifier")
)


process.vertexAndTracksCandCleaned0 = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("particleFlow"),
    veto = cms.InputTag("nuclearInteractionIdentifierAfterRefit")
)


process.vertexMerger = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveVertexFinder")
)


process.vertexRefitted = cms.EDProducer("NITrackReFitter",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("inclusiveCandidateSecondaryVertices")
)


process.vertexRefitted0 = cms.EDProducer("NITrackReFitter",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("nuclearInteractionIdentifier0")
)


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('DATA2017.root'),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep *_*_*_RECODEBUG', 
        'keep *_*_*_SIM', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_mix_MergedTrackTruth_*'
    )
)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.Chi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2'),
    MaxChi2 = cms.double(30),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.DummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('DummyDetLayerGeometry')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.FlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('FlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('LooperFittingSmoother'),
    standardFitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK')
)


process.GlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('GlobalDetLayerGeometry')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.KFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('KFFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('KFSmoother'),
    appendToDataLabel = cms.string('')
)


process.KFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.KFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('KFFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.KFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.KFUpdatorESProducer = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('KFUpdator')
)


process.LooperFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('LooperFittingSmoother'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('LooperFitter'),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('LooperSmoother'),
    appendToDataLabel = cms.string('')
)


process.LooperTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('LooperFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.LooperTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('LooperSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.MRHChi2MeasurementEstimator = cms.ESProducer("MRHChi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('MRHChi2'),
    MaxChi2 = cms.double(30.0),
    nSigma = cms.double(3.0)
)


process.MRHFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('MRHFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('MRHFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('MRHSmoother'),
    appendToDataLabel = cms.string('')
)


process.MRHTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('MRHFitter'),
    Estimator = cms.string('MRHChi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.MRHTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('MRHSmoother'),
    Estimator = cms.string('MRHChi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PixelCPEGenericESProducer = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag(""),
    PixelErrorParametrization = cms.string('NOTcmsim'),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAAlignmentOffsets = cms.bool(False),
    useLAWidthFromDB = cms.bool(True)
)


process.RK1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RK1DFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('RK1DFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RK1DSmoother'),
    appendToDataLabel = cms.string('')
)


process.RK1DTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('RK1DFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFSwitching1DUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.RK1DTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('RK1DSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFSwitching1DUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.RKFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.RKOutliers1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKOutliers1DFittingSmoother'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RK1DFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RK1DSmoother'),
    appendToDataLabel = cms.string('')
)


process.RKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('RKFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.RKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('RKSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.RungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('RungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPETemplateReco'),
    StripCPE = cms.string('StripCPEfromTrackAngle')
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.myTTRHBuilderWithoutAngle4MixedPairs = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('TTRHBuilderWithoutAngle4MixedPairs'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.myTTRHBuilderWithoutAngle4MixedTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.myTTRHBuilderWithoutAngle4PixelPairs = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.myTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    )
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.templates = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPETemplateReco'),
    DoCosmics = cms.bool(False),
    DoLorentz = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    speed = cms.int32(-2)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.ttrhbwor = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithoutRefit'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('Fake'),
    PixelCPE = cms.string('Fake'),
    StripCPE = cms.string('Fake')
)


process.ttrhbwr = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('StripCPEfromTrackAngle')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('94X_dataRun2_ReReco_EOY17_v6'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.556668),
            tmax = cms.double(10.0),
            tzero = cms.double(13.307784)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.69e-11, 7.9e-11),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.69e-11, 7.9e-11),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.inclusiveCandidateVertexingTask = cms.Task(process.candidateVertexArbitrator, process.candidateVertexMerger, process.inclusiveCandidateSecondaryVertices, process.inclusiveCandidateVertexFinder)


process.inclusiveVertexingTask = cms.Task(process.inclusiveSecondaryVertices, process.inclusiveVertexFinder, process.trackVertexArbitrator, process.vertexMerger)


process.inclusiveCandidateVertexingCvsLTask = cms.Task(process.candidateVertexArbitratorCvsL, process.candidateVertexMergerCvsL, process.inclusiveCandidateSecondaryVerticesCvsL, process.inclusiveCandidateVertexFinderCvsL)


process.inclusiveCandidateVertexingCvsL = cms.Sequence(process.inclusiveCandidateVertexingCvsLTask)


process.inclusiveCandidateVertexing = cms.Sequence(process.inclusiveCandidateVertexingTask)


process.inclusiveVertexing = cms.Sequence(process.inclusiveVertexingTask)


process.p = cms.Path(process.inclusiveCandidateVertexing+process.nuclearInteractionIdentifier0)


process.e = cms.EndPath(process.out)


