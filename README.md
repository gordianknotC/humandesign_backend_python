

## Simple Humandesign Calculator - back end
python 使用 pyephem 提供的科學計算得出所有天體資料，年代久遠(2017)結構原始，前端部份見 [front_end]。

![screen1](./src/assets/hd_screenshot.png)

__dependencies:__
 - pyephem

## Usage
```python
class Test (TestCase):
    query1 = "1985/12/30 11:45, New Taipei, Taiwan"
    query2 = "1959/5/13 7:19, Bendigo, Australia"
    query3 = "1959/5/13 7:19, New Taipei, Taiwan"

    def setUp (self):
        pass

    def tearDown (self):
        pass

    def test_parsing_date(self):
        d = Date('1985-12-30 11:45:00')
        print('lcoaltime:', localtime(d) )
        d = Date('1971-05-13 07:19:11')
        print('lcoaltime:', localtime(d                              ) )

        with self.assertRaises(OSError):
            d = Date('1969-05-23 17:19:31')
            print('lcoaltime:', localtime(d) )

        with self.assertRaises(OSError):
            d = Date('1959-05-23 17:19:31')
            print('lcoaltime:', localtime(d) )

    def test_getAstro_queryA(self):
        with self.assertRaises(UnresolvedLocalTimeError):
            result = getHDBirthChart(self.query3)

        with self.assertRaises(UnresolvedLocalTimeError):
            result = getHDBirthChart(self.query2)

        d = Date('1985/12/30 11:45')
        result = getHDBirthChart(self.query1)
        print(result)
        self.assertEqual(result, str({"personality": {"Sun": "Capricon- 8.395733338225511- 24", "Moon": "Lion- 11.139636608962661- 8", "Mercury": "Sagitarius- 20.255403840849965- 15", "Venus": "Capricon- 3.492899021107405- 30", "Mars": "Scorpio- 9.44900165020806- 27", "Jupiter": "Aquarius- 17.870544802133395- 52", "Saturn": "Sagitarius- 4.973426990959098- 58", "Uranus": "Sagitarius- 19.400798915446558- 24", "Neptune": "Capricon- 3.52538925579006- 32", "Pluto": "Scorpio- 6.8749191698062475- 52", "Chiron": "Gemini- 9.932211490887369- 56", "Vesta": "Capricon- 16.287083822630336- 17", "Pallas": "Cancer- 3.0991351928532964- 6", "Juno": "Scorpio- 27.97022547202846- 58", "Ceres": "Virgo- 16.25601291816497- 15", "North": "Torus- 8.051202181792746- 3", "South": "Scorpio- 6.6946287059833764- 42", "sunrise": "time:1985-12-31 05:49:33.084323, sign:Pices- 25.613124642573325- 37, daylong:-690, nightlong:2130", "sunset": "time:1985-12-30 18:20:16.854153, sign:Virgo- 25.613124642573325- 37, daylong:-690, nightlong:2130", "Observer": "date:1985-12-30 11:44:59.999997, lon:6959:25:54.7, lat:1433:07:35.8"}, "design": {"Sun": "Libra- 10.407159030114371- 24", "Moon": "Gemini- 1.3742694579963626- 22", "Mercury": "Libra- 18.589138712452694- 35", "Venus": "Virgo- 14.142216383337939- 9", "Mars": "Virgo- 14.944309643449998- 57", "Jupiter": "Aquarius- 7.122262987924103- 7", "Saturn": "Scorpio- 25.118050746376753- 7", "Uranus": "Sagitarius- 14.698581595801443- 42", "Neptune": "Capricon- 0.9760595947009847- 59", "Pluto": "Scorpio- 3.7204298366525848- 43", "Chiron": "Gemini- 14.002331130590605- 0", "Vesta": "Sagitarius- 0.8423912710815102- 51", "Pallas": "Cancer- 3.2956118779252677- 18", "Juno": "Libra- 28.624943547344344- 37", "Ceres": "Lion- 20.662100465091356- 40", "North": "Torus- 9.357377186599727- 21", "South": "Scorpio- 9.210703503423446- 13", "sunrise": "time:1985-10-04 05:45:46.926575, sign:Cancer- 19.026877339973524- 2, daylong:730, nightlong:710", "sunset": "time:1985-10-04 17:56:29.739390, sign:Capricon- 19.02687733997351- 2, daylong:730, nightlong:710", "Observer": "date:1985-10-04 00:23:50.748180, lon:6959:25:54.7, lat:1433:07:35.8"}}
                                     ))
```


[screen1]: src/assets/hd_screenshot.png
[screen2]: src/assets/hd_screenshot_b.png
[screen3]: src/assets/hd_screenshot_c.png
[backend]: src/
[front_end]: https://github.com/gordianknotC/humandesign_frontend_js.git












