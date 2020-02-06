# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_detects_marker_ids[2019-06-08-202719.jpg] 1'] = [
    GenericRepr('45'),
    GenericRepr('45'),
    GenericRepr('52'),
    GenericRepr('52'),
    GenericRepr('54'),
    GenericRepr('54'),
    GenericRepr('60'),
    GenericRepr('60')
]

snapshots['test_detects_marker_ids[2019-06-08-202759.jpg] 1'] = [
    GenericRepr('45'),
    GenericRepr('45'),
    GenericRepr('52'),
    GenericRepr('54'),
    GenericRepr('54'),
    GenericRepr('60'),
    GenericRepr('60')
]

snapshots['test_detects_marker_ids[2019-06-08-202825.jpg] 1'] = [
    GenericRepr('45'),
    GenericRepr('45'),
    GenericRepr('52'),
    GenericRepr('54'),
    GenericRepr('60')
]

snapshots['test_detects_marker_ids[2019-06-08-203003.jpg] 1'] = [
    GenericRepr('45'),
    GenericRepr('45'),
    GenericRepr('54'),
    GenericRepr('60')
]

snapshots['test_detects_marker_ids[2019-06-08-203035.jpg] 1'] = [
    GenericRepr('52'),
    GenericRepr('54'),
    GenericRepr('54'),
    GenericRepr('60'),
    GenericRepr('60'),
    GenericRepr('60')
]

snapshots['test_detects_marker_ids[2019-06-08-203112.jpg] 1'] = [
    GenericRepr('45'),
    GenericRepr('52'),
    GenericRepr('54'),
    GenericRepr('54'),
    GenericRepr('60')
]

snapshots['test_detects_marker_ids[2019-06-08-203132.jpg] 1'] = [
    GenericRepr('52'),
    GenericRepr('54'),
    GenericRepr('54'),
    GenericRepr('60')
]

snapshots['test_detects_marker_ids[2019-06-08-203401.jpg] 1'] = [
    GenericRepr('52'),
    GenericRepr('52'),
    GenericRepr('54'),
    GenericRepr('54'),
    GenericRepr('60'),
    GenericRepr('60')
]

snapshots['test_detects_marker_ids[2019-06-08-203608.jpg] 1'] = [
    GenericRepr('45')
]

snapshots['test_detects_marker_ids[2019-06-08-203623.jpg] 1'] = [
    GenericRepr('52')
]

snapshots['test_detects_marker_ids[2019-06-08-203643.jpg] 1'] = [
    GenericRepr('52')
]

snapshots['test_detects_marker_ids[2019-06-08-203703.jpg] 1'] = [
    GenericRepr('45'),
    GenericRepr('54')
]

snapshots['test_detects_marker_ids[2019-06-08-203821.jpg] 1'] = [
    GenericRepr('45'),
    GenericRepr('52'),
    GenericRepr('52'),
    GenericRepr('54'),
    GenericRepr('54'),
    GenericRepr('60')
]

snapshots['test_gets_markers_eager[2019-06-08-203623.jpg-C270] 1'] = [
    {
        'cartesian': [
            615.5806147830598,
            30.409062504774912,
            1801.2551702849623
        ],
        'distance': 1903,
        'id': 52,
        'orientation': (
            -3.0834514944355544,
            0.9868414899141617,
            -1.567069004962243
        ),
        'pixel_centre': [
            1251.0,
            482.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1202.0'),
                GenericRepr('355.0')
            ],
            [
                GenericRepr('1211.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('1111.0'),
                GenericRepr('532.0')
            ],
            [
                GenericRepr('1104.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.01688054783577693,
            0.3293071572758295,
            1903
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203643.jpg-C270] 1'] = [
    {
        'cartesian': [
            615.5697588577118,
            30.408983709884126,
            1801.0434339067456
        ],
        'distance': 1903,
        'id': 52,
        'orientation': (
            -3.0807214701590357,
            0.9856773390957844,
            -1.5688818243654414
        ),
        'pixel_centre': [
            1252.0,
            482.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1203.0'),
                GenericRepr('355.0')
            ],
            [
                GenericRepr('1211.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('1111.0'),
                GenericRepr('532.0')
            ],
            [
                GenericRepr('1104.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.016882488252364714,
            0.32933773534056865,
            1903
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-202719.jpg-C270] 1'] = [
    {
        'cartesian': [
            48.97247358170491,
            -43.540491875278086,
            2267.382873156615
        ],
        'distance': 2268,
        'id': 54,
        'orientation': (
            -2.374775138098944,
            -0.009807428993270965,
            1.7362260197255788
        ),
        'pixel_centre': [
            207.0,
            239.0
        ],
        'pixel_corners': [
            [
                GenericRepr('158.0'),
                GenericRepr('379.0')
            ],
            [
                GenericRepr('139.0'),
                GenericRepr('301.0')
            ],
            [
                GenericRepr('246.0'),
                GenericRepr('289.0')
            ],
            [
                GenericRepr('259.0'),
                GenericRepr('367.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.019200613033588776,
            0.02159532076609588,
            2268
        )
    },
    {
        'cartesian': [
            38.621549153972964,
            -137.80162512034136,
            2333.0145288597682
        ],
        'distance': 2337,
        'id': 54,
        'orientation': (
            2.1605344813034515,
            -0.12187790230224262,
            3.130920068765706
        ),
        'pixel_centre': [
            290.0,
            166.0
        ],
        'pixel_corners': [
            [
                GenericRepr('241.0'),
                GenericRepr('259.0')
            ],
            [
                GenericRepr('136.0'),
                GenericRepr('270.0')
            ],
            [
                GenericRepr('139.0'),
                GenericRepr('216.0')
            ],
            [
                GenericRepr('237.0'),
                GenericRepr('207.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.05899736361515225,
            0.016552842350917953,
            2337
        )
    },
    {
        'cartesian': [
            225.15552374510497,
            149.15209372976605,
            2058.5813186709834
        ],
        'distance': 2076,
        'id': 52,
        'orientation': (
            -2.340785501297267,
            -0.07367321031068015,
            0.10059263412692815
        ),
        'pixel_centre': [
            400.0,
            553.0
        ],
        'pixel_corners': [
            [
                GenericRepr('351.0'),
                GenericRepr('522.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('525.0')
            ],
            [
                GenericRepr('474.0'),
                GenericRepr('603.0')
            ],
            [
                GenericRepr('358.0'),
                GenericRepr('604.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.07232744086108522,
            0.10894108910495433,
            2076
        )
    },
    {
        'cartesian': [
            232.6617149320773,
            55.539256082026675,
            2084.684736553089
        ],
        'distance': 2098,
        'id': 52,
        'orientation': (
            2.2310366500853216,
            -0.12512995161344634,
            2.980443908823364
        ),
        'pixel_centre': [
            523.0,
            360.0
        ],
        'pixel_corners': [
            [
                GenericRepr('474.0'),
                GenericRepr('489.0')
            ],
            [
                GenericRepr('354.0'),
                GenericRepr('487.0')
            ],
            [
                GenericRepr('365.0'),
                GenericRepr('410.0')
            ],
            [
                GenericRepr('478.0'),
                GenericRepr('413.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.026635260774595937,
            0.11114528555036168,
            2098
        )
    },
    {
        'cartesian': [
            579.2978057029335,
            -88.94695650886655,
            2770.9294952039127
        ],
        'distance': 2832,
        'id': 60,
        'orientation': (
            -2.511251547498965,
            -0.38631806341066616,
            0.06936643203800477
        ),
        'pixel_centre': [
            659.0,
            302.0
        ],
        'pixel_corners': [
            [
                GenericRepr('610.0'),
                GenericRepr('262.0')
            ],
            [
                GenericRepr('703.0'),
                GenericRepr('277.0')
            ],
            [
                GenericRepr('697.0'),
                GenericRepr('352.0')
            ],
            [
                GenericRepr('608.0'),
                GenericRepr('337.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.032089024583045085,
            0.2060942464482809,
            2832
        )
    },
    {
        'cartesian': [
            618.1004750940332,
            -194.6624239721691,
            2869.457529588602
        ],
        'distance': 2941,
        'id': 60,
        'orientation': (
            2.2425686591916687,
            -0.05607015160098767,
            2.780934796976062
        ),
        'pixel_centre': [
            756.0,
            139.0
        ],
        'pixel_corners': [
            [
                GenericRepr('707.0'),
                GenericRepr('250.0')
            ],
            [
                GenericRepr('615.0'),
                GenericRepr('236.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('189.0')
            ],
            [
                GenericRepr('723.0'),
                GenericRepr('202.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.06773566756178286,
            0.21216489101779432,
            2941
        )
    },
    {
        'cartesian': [
            940.1588374368113,
            224.43899142207056,
            3108.420708301315
        ],
        'distance': 3255,
        'id': 45,
        'orientation': (
            -2.6905576238675173,
            0.35601013314439545,
            2.9899714705455573
        ),
        'pixel_centre': [
            1060.0,
            500.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1011.0'),
                GenericRepr('639.0')
            ],
            [
                GenericRepr('896.0'),
                GenericRepr('629.0')
            ],
            [
                GenericRepr('916.0'),
                GenericRepr('550.0')
            ],
            [
                GenericRepr('1037.0'),
                GenericRepr('560.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.07207846088374699,
            0.29370799143453274,
            3255
        )
    },
    {
        'cartesian': [
            1049.5881203039353,
            108.63429004043235,
            3428.3895118517153
        ],
        'distance': 3587,
        'id': 45,
        'orientation': (
            2.9291313262640166,
            0.2475668396986916,
            -1.5803413376036526
        ),
        'pixel_centre': [
            1064.0,
            465.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1015.0'),
                GenericRepr('446.0')
            ],
            [
                GenericRepr('1034.0'),
                GenericRepr('528.0')
            ],
            [
                GenericRepr('913.0'),
                GenericRepr('515.0')
            ],
            [
                GenericRepr('902.0'),
                GenericRepr('436.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.031676083950300755,
            0.2970858479527087,
            3587
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-202759.jpg-C270] 1'] = [
    {
        'cartesian': [
            145.74373036840615,
            -40.256101048113365,
            1695.8865525211438
        ],
        'distance': 1702,
        'id': 54,
        'orientation': (
            -2.021155971629812,
            -0.1928500018914251,
            1.813522035967637
        ),
        'pixel_centre': [
            349.0,
            243.0
        ],
        'pixel_corners': [
            [
                GenericRepr('300.0'),
                GenericRepr('354.0')
            ],
            [
                GenericRepr('271.0'),
                GenericRepr('284.0')
            ],
            [
                GenericRepr('415.0'),
                GenericRepr('293.0')
            ],
            [
                GenericRepr('433.0'),
                GenericRepr('363.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.023733039527514883,
            0.08572891261099974,
            1702
        )
    },
    {
        'cartesian': [
            143.68573293688746,
            -134.99106597506574,
            1665.9077085539982
        ],
        'distance': 1677,
        'id': 54,
        'orientation': (
            2.5642693646694017,
            -0.17430626778660732,
            2.932965520289589
        ),
        'pixel_centre': [
            465.0,
            73.0
        ],
        'pixel_corners': [
            [
                GenericRepr('416.0'),
                GenericRepr('249.0')
            ],
            [
                GenericRepr('271.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('297.0'),
                GenericRepr('123.0')
            ],
            [
                GenericRepr('435.0'),
                GenericRepr('132.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.08085488075673547,
            0.08603778740109605,
            1677
        )
    },
    {
        'cartesian': [
            142.89344515411798,
            126.15052127191359,
            1416.1887644677813
        ],
        'distance': 1428,
        'id': 52,
        'orientation': (
            2.5408392198729035,
            -0.2964381644472136,
            2.9899950612903115
        ),
        'pixel_centre': [
            524.0,
            477.0
        ],
        'pixel_corners': [
            [
                GenericRepr('475.0'),
                GenericRepr('689.0')
            ],
            [
                GenericRepr('301.0'),
                GenericRepr('689.0')
            ],
            [
                GenericRepr('320.0'),
                GenericRepr('527.0')
            ],
            [
                GenericRepr('483.0'),
                GenericRepr('529.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.08884298789037894,
            0.10055966114207664,
            1428
        )
    },
    {
        'cartesian': [
            495.37653019908004,
            -92.71839331607553,
            2086.756057805681
        ],
        'distance': 2146,
        'id': 60,
        'orientation': (
            -2.146688086504218,
            -0.15376856564237784,
            0.13250201533075248
        ),
        'pixel_centre': [
            714.0,
            265.0
        ],
        'pixel_corners': [
            [
                GenericRepr('665.0'),
                GenericRepr('238.0')
            ],
            [
                GenericRepr('805.0'),
                GenericRepr('243.0')
            ],
            [
                GenericRepr('791.0'),
                GenericRepr('315.0')
            ],
            [
                GenericRepr('661.0'),
                GenericRepr('309.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.04440262705270071,
            0.2330763563068217,
            2146
        )
    },
    {
        'cartesian': [
            485.8525286176275,
            -197.6108472448464,
            2040.2058111030517
        ],
        'distance': 2106,
        'id': 60,
        'orientation': (
            2.7450103543587057,
            0.08918522900956188,
            3.0779710073436153
        ),
        'pixel_centre': [
            854.0,
            36.0
        ],
        'pixel_corners': [
            [
                GenericRepr('805.0'),
                GenericRepr('203.0')
            ],
            [
                GenericRepr('664.0'),
                GenericRepr('197.0')
            ],
            [
                GenericRepr('669.0'),
                GenericRepr('86.0')
            ],
            [
                GenericRepr('804.0'),
                GenericRepr('92.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.09655709123623162,
            0.23378457466325744,
            2106
        )
    },
    {
        'cartesian': [
            673.6284363791592,
            183.85764494825509,
            2410.542678086448
        ],
        'distance': 2509,
        'id': 45,
        'orientation': (
            1.8840792107646445,
            -0.2865274976792751,
            2.6473169753369916
        ),
        'pixel_centre': [
            984.0,
            517.0
        ],
        'pixel_corners': [
            [
                GenericRepr('935.0'),
                GenericRepr('627.0')
            ],
            [
                GenericRepr('791.0'),
                GenericRepr('617.0')
            ],
            [
                GenericRepr('811.0'),
                GenericRepr('567.0')
            ],
            [
                GenericRepr('970.0'),
                GenericRepr('577.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.0761249147287415,
            0.2724994947028334,
            2509
        )
    },
    {
        'cartesian': [
            534.5034319853727,
            46.41496320872599,
            1871.284594446041
        ],
        'distance': 1946,
        'id': 45,
        'orientation': (
            3.1288802071645088,
            0.41829537250197435,
            -1.6007313539829524
        ),
        'pixel_centre': [
            1009.0,
            474.0
        ],
        'pixel_corners': [
            [
                GenericRepr('960.0'),
                GenericRepr('392.0')
            ],
            [
                GenericRepr('969.0'),
                GenericRepr('536.0')
            ],
            [
                GenericRepr('808.0'),
                GenericRepr('524.0')
            ],
            [
                GenericRepr('807.0'),
                GenericRepr('382.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.024798712209911596,
            0.2782258895906213,
            1946
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-202825.jpg-C270] 1'] = [
    {
        'cartesian': [
            113.50031115128753,
            -248.6544685541128,
            4995.715426354672
        ],
        'distance': 5003,
        'id': 52,
        'orientation': (
            2.8020065399053813,
            -0.1341033851011886,
            0.1159768707354907
        ),
        'pixel_centre': [
            226.0,
            229.0
        ],
        'pixel_corners': [
            [
                GenericRepr('177.0'),
                GenericRepr('242.0')
            ],
            [
                GenericRepr('223.0'),
                GenericRepr('234.0')
            ],
            [
                GenericRepr('230.0'),
                GenericRepr('279.0')
            ],
            [
                GenericRepr('182.0'),
                GenericRepr('286.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.0497325032941344,
            0.022715623040754706,
            5003
        )
    },
    {
        'cartesian': [
            437.14331427744634,
            36.11418563006483,
            3719.93984313552
        ],
        'distance': 3745,
        'id': 45,
        'orientation': (
            1.9246362915541546,
            -0.06308216454554283,
            0.0619012595336596
        ),
        'pixel_centre': [
            443.0,
            367.0
        ],
        'pixel_corners': [
            [
                GenericRepr('394.0'),
                GenericRepr('398.0')
            ],
            [
                GenericRepr('457.0'),
                GenericRepr('393.0')
            ],
            [
                GenericRepr('470.0'),
                GenericRepr('417.0')
            ],
            [
                GenericRepr('404.0'),
                GenericRepr('421.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.009707966425076632,
            0.11697705039027918,
            3745
        )
    },
    {
        'cartesian': [
            438.9721413021396,
            122.79979847441793,
            3630.597292416694
        ],
        'distance': 3659,
        'id': 45,
        'orientation': (
            -2.672136565431361,
            0.12379183782061447,
            0.04930034366911938
        ),
        'pixel_centre': [
            456.0,
            444.0
        ],
        'pixel_corners': [
            [
                GenericRepr('407.0'),
                GenericRepr('440.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('434.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('494.0')
            ],
            [
                GenericRepr('408.0'),
                GenericRepr('500.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.033810690537705065,
            0.12032499440047467,
            3659
        )
    },
    {
        'cartesian': [
            1319.4297482330408,
            -237.21862472588327,
            5549.346373593318
        ],
        'distance': 5708,
        'id': 60,
        'orientation': (
            3.130901978771658,
            0.1033472544638747,
            1.5343295620823738
        ),
        'pixel_centre': [
            753.0,
            210.0
        ],
        'pixel_corners': [
            [
                GenericRepr('704.0'),
                GenericRepr('303.0')
            ],
            [
                GenericRepr('705.0'),
                GenericRepr('258.0')
            ],
            [
                GenericRepr('753.0'),
                GenericRepr('260.0')
            ],
            [
                GenericRepr('751.0'),
                GenericRepr('305.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.04272111988817821,
            0.23342882954994468,
            5708
        )
    },
    {
        'cartesian': [
            1539.1078609047545,
            -85.75371591622213,
            5206.422170013941
        ],
        'distance': 5429,
        'id': 54,
        'orientation': (
            3.0847199591610925,
            0.5060232477609161,
            3.028944535387404
        ),
        'pixel_centre': [
            987.0,
            270.0
        ],
        'pixel_corners': [
            [
                GenericRepr('938.0'),
                GenericRepr('378.0')
            ],
            [
                GenericRepr('883.0'),
                GenericRepr('370.0')
            ],
            [
                GenericRepr('888.0'),
                GenericRepr('320.0')
            ],
            [
                GenericRepr('943.0'),
                GenericRepr('327.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.01646926810550821,
            0.2874310279409345,
            5429
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203003.jpg-C270] 1'] = [
    {
        'cartesian': [
            20.48851199982102,
            95.69566069733483,
            1580.5788190031387
        ],
        'distance': 1583,
        'id': 45,
        'orientation': (
            -2.5848888249788726,
            -1.0496249961048107,
            1.9683197477307306
        ),
        'pixel_centre': [
            209.0,
            415.0
        ],
        'pixel_corners': [
            [
                GenericRepr('160.0'),
                GenericRepr('593.0')
            ],
            [
                GenericRepr('130.0'),
                GenericRepr('448.0')
            ],
            [
                GenericRepr('203.0'),
                GenericRepr('465.0')
            ],
            [
                GenericRepr('231.0'),
                GenericRepr('623.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.06047087737739141,
            0.012961937932580238,
            1583
        )
    },
    {
        'cartesian': [
            115.09648190599003,
            82.89109754682602,
            1525.4457324445514
        ],
        'distance': 1532,
        'id': 45,
        'orientation': (
            -2.9060264302941743,
            0.4133142759398382,
            1.7714497542688457
        ),
        'pixel_centre': [
            325.0,
            370.0
        ],
        'pixel_corners': [
            [
                GenericRepr('276.0'),
                GenericRepr('620.0')
            ],
            [
                GenericRepr('246.0'),
                GenericRepr('463.0')
            ],
            [
                GenericRepr('387.0'),
                GenericRepr('420.0')
            ],
            [
                GenericRepr('411.0'),
                GenericRepr('566.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.05428554768457168,
            0.07530835941656067,
            1532
        )
    },
    {
        'cartesian': [
            289.91616050097764,
            -212.77135366250374,
            1991.8391295376969
        ],
        'distance': 2024,
        'id': 60,
        'orientation': (
            2.3558760516232677,
            -0.10217370213786375,
            1.7257551854534197
        ),
        'pixel_centre': [
            501.0,
            26.0
        ],
        'pixel_corners': [
            [
                GenericRepr('452.0'),
                GenericRepr('172.0')
            ],
            [
                GenericRepr('423.0'),
                GenericRepr('96.0')
            ],
            [
                GenericRepr('539.0'),
                GenericRepr('76.0')
            ],
            [
                GenericRepr('573.0'),
                GenericRepr('150.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.10641800652759896,
            0.14453700829579358,
            2024
        )
    },
    {
        'cartesian': [
            583.5382492994955,
            0.8816396212834946,
            1943.5842622796292
        ],
        'distance': 2029,
        'id': 54,
        'orientation': (
            -3.080013487331484,
            0.5672894694515732,
            1.6484831876888573
        ),
        'pixel_centre': [
            921.0,
            268.0
        ],
        'pixel_corners': [
            [
                GenericRepr('872.0'),
                GenericRepr('469.0')
            ],
            [
                GenericRepr('859.0'),
                GenericRepr('332.0')
            ],
            [
                GenericRepr('1006.0'),
                GenericRepr('318.0')
            ],
            [
                GenericRepr('1016.0'),
                GenericRepr('458.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.00045361530133953935,
            0.29167531643278244,
            2029
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203035.jpg-C270] 1'] = [
    {
        'cartesian': [
            164.77687930600482,
            -144.46545080882265,
            1817.7412559756758
        ],
        'distance': 1830,
        'id': 60,
        'orientation': (
            2.07661357474768,
            -0.2871784941821913,
            1.2467481609809512
        ),
        'pixel_centre': [
            335.0,
            100.0
        ],
        'pixel_corners': [
            [
                GenericRepr('286.0'),
                GenericRepr('228.0')
            ],
            [
                GenericRepr('320.0'),
                GenericRepr('165.0')
            ],
            [
                GenericRepr('441.0'),
                GenericRepr('150.0')
            ],
            [
                GenericRepr('414.0'),
                GenericRepr('214.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.07930855654857982,
            0.09040216887952719,
            1830
        )
    },
    {
        'cartesian': [
            161.4722561665811,
            -50.73479763501068,
            1768.2769166205892
        ],
        'distance': 1776,
        'id': 60,
        'orientation': (
            -2.47467891707711,
            -0.2870130010351253,
            1.8918627704858753
        ),
        'pixel_centre': [
            372.0,
            198.0
        ],
        'pixel_corners': [
            [
                GenericRepr('323.0'),
                GenericRepr('373.0')
            ],
            [
                GenericRepr('284.0'),
                GenericRepr('262.0')
            ],
            [
                GenericRepr('416.0'),
                GenericRepr('248.0')
            ],
            [
                GenericRepr('448.0'),
                GenericRepr('363.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.02868378940620112,
            0.09106360388030527,
            1776
        )
    },
    {
        'cartesian': [
            264.2288895455216,
            -101.68069930155195,
            1908.5136086971556
        ],
        'distance': 1929,
        'id': 60,
        'orientation': (
            2.9194815679237767,
            1.1567369967876822,
            0.8230141052240988
        ),
        'pixel_centre': [
            503.0,
            222.0
        ],
        'pixel_corners': [
            [
                GenericRepr('454.0'),
                GenericRepr('233.0')
            ],
            [
                GenericRepr('476.0'),
                GenericRepr('166.0')
            ],
            [
                GenericRepr('504.0'),
                GenericRepr('272.0')
            ],
            [
                GenericRepr('485.0'),
                GenericRepr('342.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.05322710615864915,
            0.1375729372306014,
            1929
        )
    },
    {
        'cartesian': [
            256.23826211599015,
            66.70634334627935,
            1866.8194079498799
        ],
        'distance': 1885,
        'id': 52,
        'orientation': (
            3.089916374673172,
            1.1600914467598487,
            0.06401960891380874
        ),
        'pixel_centre': [
            508.0,
            484.0
        ],
        'pixel_corners': [
            [
                GenericRepr('459.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('495.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('500.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('465.0'),
                GenericRepr('546.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.03571742083320784,
            0.13640688796818903,
            1885
        )
    },
    {
        'cartesian': [
            267.83153094388206,
            56.58993306294073,
            1364.5048481694275
        ],
        'distance': 1391,
        'id': 54,
        'orientation': (
            2.9931084840564655,
            -0.784745976343979,
            1.5286223252515483
        ),
        'pixel_centre': [
            602.0,
            345.0
        ],
        'pixel_corners': [
            [
                GenericRepr('553.0'),
                GenericRepr('582.0')
            ],
            [
                GenericRepr('549.0'),
                GenericRepr('403.0')
            ],
            [
                GenericRepr('705.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('710.0'),
                GenericRepr('587.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.041449117388438136,
            0.19382069191808782,
            1391
        )
    },
    {
        'cartesian': [
            374.23985428691486,
            52.46482598758089,
            1430.589614052576
        ],
        'distance': 1479,
        'id': 54,
        'orientation': (
            -3.0833799621112803,
            0.964853309201618,
            -0.0040733153394813286
        ),
        'pixel_centre': [
            810.0,
            517.0
        ],
        'pixel_corners': [
            [
                GenericRepr('761.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('837.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('844.0'),
                GenericRepr('567.0')
            ],
            [
                GenericRepr('768.0'),
                GenericRepr('586.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.03665714022261602,
            0.2558645995142081,
            1479
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203112.jpg-C270] 1'] = [
    {
        'cartesian': [
            739.0535497132768,
            55.98058016808598,
            5648.073707934236
        ],
        'distance': 5696,
        'id': 45,
        'orientation': (
            -2.742018530298092,
            0.12260529728945267,
            -3.079420435154583
        ),
        'pixel_centre': [
            534.0,
            340.0
        ],
        'pixel_corners': [
            [
                GenericRepr('485.0'),
                GenericRepr('426.0')
            ],
            [
                GenericRepr('443.0'),
                GenericRepr('430.0')
            ],
            [
                GenericRepr('442.0'),
                GenericRepr('390.0')
            ],
            [
                GenericRepr('484.0'),
                GenericRepr('386.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.009911121924691738,
            0.1301113272642795,
            5696
        )
    },
    {
        'cartesian': [
            1306.1800442841482,
            -1.2842532389681658,
            6257.381731580902
        ],
        'distance': 6392,
        'id': 52,
        'orientation': (
            2.9216787995329607,
            -0.47615646393344757,
            -0.029168877915175397
        ),
        'pixel_centre': [
            683.0,
            355.0
        ],
        'pixel_corners': [
            [
                GenericRepr('634.0'),
                GenericRepr('368.0')
            ],
            [
                GenericRepr('673.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('675.0'),
                GenericRepr('405.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('407.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.00020523811332374002,
            0.20578727969670024,
            6392
        )
    },
    {
        'cartesian': [
            1750.2757816336425,
            -11.22994181322708,
            6616.916317181946
        ],
        'distance': 6844,
        'id': 60,
        'orientation': (
            -2.956769882623342,
            0.3613927869046201,
            -1.562310930346238
        ),
        'pixel_centre': [
            875.0,
            356.0
        ],
        'pixel_corners': [
            [
                GenericRepr('826.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('825.0'),
                GenericRepr('404.0')
            ],
            [
                GenericRepr('786.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('787.0'),
                GenericRepr('368.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.0016971547610582774,
            0.2585928057281205,
            6844
        )
    },
    {
        'cartesian': [
            2052.310983638644,
            4.816825291705704,
            6747.310697435263
        ],
        'distance': 7052,
        'id': 54,
        'orientation': (
            3.071969336115055,
            0.7015455718209448,
            -1.6967004469974478
        ),
        'pixel_centre': [
            1016.0,
            361.0
        ],
        'pixel_corners': [
            [
                GenericRepr('967.0'),
                GenericRepr('379.0')
            ],
            [
                GenericRepr('965.0'),
                GenericRepr('419.0')
            ],
            [
                GenericRepr('929.0'),
                GenericRepr('411.0')
            ],
            [
                GenericRepr('931.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.0007138880495395767,
            0.2952755670543514,
            7052
        )
    },
    {
        'cartesian': [
            2165.8879753672495,
            1.8969081407824882,
            6909.813197168766
        ],
        'distance': 7241,
        'id': 54,
        'orientation': (
            1.382196065375173,
            -1.4477970625090455,
            0.06103582713672187
        ),
        'pixel_centre': [
            1027.0,
            321.0
        ],
        'pixel_corners': [
            [
                GenericRepr('978.0'),
                GenericRepr('419.0')
            ],
            [
                GenericRepr('980.0'),
                GenericRepr('380.0')
            ],
            [
                GenericRepr('1001.0'),
                GenericRepr('371.0')
            ],
            [
                GenericRepr('999.0'),
                GenericRepr('409.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.0002745237879813167,
            0.303751040775963,
            7241
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203132.jpg-C270] 1'] = [
    {
        'cartesian': [
            1402.321068606438,
            -170.8835226211283,
            7210.4523971705175
        ],
        'distance': 7347,
        'id': 52,
        'orientation': (
            -3.0002956773507803,
            0.038872548559657924,
            0.04110850629582092
        ),
        'pixel_centre': [
            649.0,
            294.0
        ],
        'pixel_corners': [
            [
                GenericRepr('600.0'),
                GenericRepr('311.0')
            ],
            [
                GenericRepr('634.0'),
                GenericRepr('310.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('344.0')
            ],
            [
                GenericRepr('601.0'),
                GenericRepr('345.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.023694982095134886,
            0.19208659176797196,
            7347
        )
    },
    {
        'cartesian': [
            1807.8840602046369,
            -180.57348228893426,
            7386.732183680077
        ],
        'distance': 7606,
        'id': 60,
        'orientation': (
            -3.0906780369789457,
            0.2556989107409489,
            -1.5382122335842452
        ),
        'pixel_centre': [
            813.0,
            295.0
        ],
        'pixel_corners': [
            [
                GenericRepr('764.0'),
                GenericRepr('310.0')
            ],
            [
                GenericRepr('765.0'),
                GenericRepr('344.0')
            ],
            [
                GenericRepr('731.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('730.0'),
                GenericRepr('311.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.024440783970798935,
            0.2400290346120365,
            7606
        )
    },
    {
        'cartesian': [
            2020.3377600043916,
            -177.7299037662553,
            7145.636440902925
        ],
        'distance': 7427,
        'id': 54,
        'orientation': (
            -3.0395584730123235,
            -1.3221403997335517,
            -1.4857778259817267
        ),
        'pixel_centre': [
            926.0,
            295.0
        ],
        'pixel_corners': [
            [
                GenericRepr('877.0'),
                GenericRepr('308.0')
            ],
            [
                GenericRepr('878.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('852.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('852.0'),
                GenericRepr('309.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.024867381437367313,
            0.27554516722893785,
            7427
        )
    },
    {
        'cartesian': [
            2156.67287730126,
            -181.68124733650623,
            7362.175283051346
        ],
        'distance': 7673,
        'id': 54,
        'orientation': (
            3.1357278920429774,
            0.786524820056796,
            1.5856417660454294
        ),
        'pixel_centre': [
            938.0,
            259.0
        ],
        'pixel_corners': [
            [
                GenericRepr('889.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('889.0'),
                GenericRepr('309.0')
            ],
            [
                GenericRepr('915.0'),
                GenericRepr('309.0')
            ],
            [
                GenericRepr('915.0'),
                GenericRepr('345.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.024672650857571036,
            0.2849668671254678,
            7673
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203401.jpg-C270] 1'] = [
    {
        'cartesian': [
            -4.278651489335534,
            -79.85031016359937,
            1858.3067132121755
        ],
        'distance': 1860,
        'id': 54,
        'orientation': (
            -3.1070218011670905,
            -1.029871556831879,
            1.610886372213291
        ),
        'pixel_centre': [
            161.0,
            156.0
        ],
        'pixel_corners': [
            [
                GenericRepr('112.0'),
                GenericRepr('343.0')
            ],
            [
                GenericRepr('110.0'),
                GenericRepr('216.0')
            ],
            [
                GenericRepr('175.0'),
                GenericRepr('206.0')
            ],
            [
                GenericRepr('179.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.0429429757731973,
            -0.0023024422708009026,
            1860
        )
    },
    {
        'cartesian': [
            99.73491563380324,
            -80.83431302830807,
            1883.9280979514065
        ],
        'distance': 1888,
        'id': 54,
        'orientation': (
            3.0845148562765057,
            0.439149506167336,
            1.589798231134693
        ),
        'pixel_centre': [
            269.0,
            167.0
        ],
        'pixel_corners': [
            [
                GenericRepr('220.0'),
                GenericRepr('342.0')
            ],
            [
                GenericRepr('217.0'),
                GenericRepr('209.0')
            ],
            [
                GenericRepr('329.0'),
                GenericRepr('217.0')
            ],
            [
                GenericRepr('332.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.04288102156410237,
            0.052890499772393275,
            1888
        )
    },
    {
        'cartesian': [
            571.9480775930399,
            -100.13985450608754,
            2537.4457478715563
        ],
        'distance': 2603,
        'id': 52,
        'orientation': (
            -3.0804016768844367,
            -1.3207359741550995,
            -1.5154912516162953
        ),
        'pixel_centre': [
            768.0,
            288.0
        ],
        'pixel_corners': [
            [
                GenericRepr('719.0'),
                GenericRepr('237.0')
            ],
            [
                GenericRepr('721.0'),
                GenericRepr('339.0')
            ],
            [
                GenericRepr('673.0'),
                GenericRepr('338.0')
            ],
            [
                GenericRepr('671.0'),
                GenericRepr('244.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.03944435650004852,
            0.2216980630685447,
            2603
        )
    },
    {
        'cartesian': [
            654.6310366779835,
            -99.487531298726,
            2522.14085896417
        ],
        'distance': 2607,
        'id': 52,
        'orientation': (
            -3.137416617450789,
            0.571909844470826,
            0.012538399281592663
        ),
        'pixel_centre': [
            798.0,
            289.0
        ],
        'pixel_corners': [
            [
                GenericRepr('749.0'),
                GenericRepr('238.0')
            ],
            [
                GenericRepr('834.0'),
                GenericRepr('240.0')
            ],
            [
                GenericRepr('833.0'),
                GenericRepr('339.0')
            ],
            [
                GenericRepr('750.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.039425228571153895,
            0.25394998931733404,
            2607
        )
    },
    {
        'cartesian': [
            871.509902412247,
            -107.71556170719587,
            2839.9736712721833
        ],
        'distance': 2972,
        'id': 60,
        'orientation': (
            3.1012797750302674,
            0.7136259604963243,
            0.045122095115882666
        ),
        'pixel_centre': [
            968.0,
            288.0
        ],
        'pixel_corners': [
            [
                GenericRepr('919.0'),
                GenericRepr('244.0')
            ],
            [
                GenericRepr('1007.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('1007.0'),
                GenericRepr('338.0')
            ],
            [
                GenericRepr('920.0'),
                GenericRepr('338.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.03791019456696663,
            0.29774988008937725,
            2972
        )
    },
    {
        'cartesian': [
            978.996763122183,
            -110.84414638308169,
            3003.908029285937
        ],
        'distance': 3161,
        'id': 60,
        'orientation': (
            3.087021382651743,
            1.0477415847164546,
            1.6107958207438398
        ),
        'pixel_centre': [
            1084.0,
            193.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1035.0'),
                GenericRepr('337.0')
            ],
            [
                GenericRepr('1038.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('1078.0'),
                GenericRepr('243.0')
            ],
            [
                GenericRepr('1075.0'),
                GenericRepr('337.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.03688324595332467,
            0.3150526654021497,
            3161
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203608.jpg-C270] 1'] = [
    {
        'cartesian': [
            289.3794123983702,
            44.90973876434696,
            1667.02945692283
        ],
        'distance': 1692,
        'id': 45,
        'orientation': (
            -2.9669046217884048,
            0.029697412152458445,
            3.136952675256492
        ),
        'pixel_centre': [
            691.0,
            327.0
        ],
        'pixel_corners': [
            [
                GenericRepr('642.0'),
                GenericRepr('527.0')
            ],
            [
                GenericRepr('494.0'),
                GenericRepr('525.0')
            ],
            [
                GenericRepr('497.0'),
                GenericRepr('377.0')
            ],
            [
                GenericRepr('643.0'),
                GenericRepr('381.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.02693346461603209,
            0.17187710326698852,
            1692
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203703.jpg-C270] 1'] = [
    {
        'cartesian': [
            252.60114340531564,
            35.22710808642984,
            1564.5526920054965
        ],
        'distance': 1585,
        'id': 54,
        'orientation': (
            -3.0380749401807705,
            0.0965837203503277,
            1.5520533833009578
        ),
        'pixel_centre': [
            509.0,
            315.0
        ],
        'pixel_corners': [
            [
                GenericRepr('460.0'),
                GenericRepr('519.0')
            ],
            [
                GenericRepr('464.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('616.0'),
                GenericRepr('365.0')
            ],
            [
                GenericRepr('615.0'),
                GenericRepr('521.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.02251196598635397,
            0.16007130906483927,
            1585
        )
    },
    {
        'cartesian': [
            574.540259387511,
            37.73958423026057,
            1826.439594271735
        ],
        'distance': 1915,
        'id': 45,
        'orientation': (
            -3.0732684123695253,
            0.6663673324368136,
            3.1212367933221548
        ),
        'pixel_centre': [
            1136.0,
            325.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1087.0'),
                GenericRepr('531.0')
            ],
            [
                GenericRepr('928.0'),
                GenericRepr('528.0')
            ],
            [
                GenericRepr('926.0'),
                GenericRepr('375.0')
            ],
            [
                GenericRepr('1083.0'),
                GenericRepr('376.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.020659984962508707,
            0.30476817491846736,
            1915
        )
    }
]

snapshots['test_gets_markers_eager[2019-06-08-203821.jpg-C270] 1'] = [
    {
        'cartesian': [
            10.815163830753228,
            37.76793500472289,
            1974.9929815172177
        ],
        'distance': 1975,
        'id': 54,
        'orientation': (
            2.9868779877922615,
            -1.249462509947138,
            1.5179269813414156
        ),
        'pixel_centre': [
            191.0,
            309.0
        ],
        'pixel_corners': [
            [
                GenericRepr('142.0'),
                GenericRepr('493.0')
            ],
            [
                GenericRepr('144.0'),
                GenericRepr('374.0')
            ],
            [
                GenericRepr('183.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('181.0'),
                GenericRepr('489.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.019120742482849687,
            0.0054759970433421595,
            1975
        )
    },
    {
        'cartesian': [
            108.5141149534567,
            34.39746973212966,
            1942.0425675367171
        ],
        'distance': 1945,
        'id': 54,
        'orientation': (
            3.1189092194694097,
            0.12172677650268669,
            1.5585483680942989
        ),
        'pixel_centre': [
            270.0,
            316.0
        ],
        'pixel_corners': [
            [
                GenericRepr('221.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('222.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('344.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('344.0'),
                GenericRepr('488.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.01771015423730071,
            0.055818237503316076,
            1945
        )
    },
    {
        'cartesian': [
            441.4274189102652,
            41.66715995536204,
            2209.653485557894
        ],
        'distance': 2253,
        'id': 45,
        'orientation': (
            -3.0376327923058386,
            0.15704574314351033,
            3.1330619367295203
        ),
        'pixel_centre': [
            736.0,
            326.0
        ],
        'pixel_corners': [
            [
                GenericRepr('687.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('579.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('579.0'),
                GenericRepr('376.0')
            ],
            [
                GenericRepr('688.0'),
                GenericRepr('379.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.01885464059740423,
            0.197176546986623,
            2253
        )
    },
    {
        'cartesian': [
            658.0691640734908,
            36.039073017784744,
            2280.2029485188013
        ],
        'distance': 2373,
        'id': 60,
        'orientation': (
            -3.078347935477998,
            0.5366682921909237,
            1.571842828376763
        ),
        'pixel_centre': [
            884.0,
            325.0
        ],
        'pixel_corners': [
            [
                GenericRepr('835.0'),
                GenericRepr('492.0')
            ],
            [
                GenericRepr('833.0'),
                GenericRepr('377.0')
            ],
            [
                GenericRepr('948.0'),
                GenericRepr('375.0')
            ],
            [
                GenericRepr('952.0'),
                GenericRepr('493.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.01580388823882312,
            0.28096659490260334,
            2373
        )
    },
    {
        'cartesian': [
            776.4373597699536,
            26.923240002553833,
            2357.163003644615
        ],
        'distance': 2481,
        'id': 52,
        'orientation': (
            -3.1013369352130016,
            0.9603254047449361,
            -1.557961959218717
        ),
        'pixel_centre': [
            1159.0,
            440.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1110.0'),
                GenericRepr('362.0')
            ],
            [
                GenericRepr('1116.0'),
                GenericRepr('491.0')
            ],
            [
                GenericRepr('1042.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('1037.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.011421386325802158,
            0.31820174339863255,
            2481
        )
    },
    {
        'cartesian': [
            847.6035102161021,
            24.61107745691945,
            2426.701306243966
        ],
        'distance': 2570,
        'id': 52,
        'orientation': (
            -3.1096390185608778,
            0.8971191200096716,
            -0.023410523590355805
        ),
        'pixel_centre': [
            1201.0,
            444.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1152.0'),
                GenericRepr('363.0')
            ],
            [
                GenericRepr('1260.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('1263.0'),
                GenericRepr('494.0')
            ],
            [
                GenericRepr('1155.0'),
                GenericRepr('493.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.010141435061934545,
            0.33603518852250885,
            2570
        )
    }
]

snapshots['test_gets_markers[2019-06-08-202719.jpg] 1'] = [
    {
        'id': 54,
        'pixel_centre': [
            207.0,
            239.0
        ],
        'pixel_corners': [
            [
                GenericRepr('158.0'),
                GenericRepr('379.0')
            ],
            [
                GenericRepr('139.0'),
                GenericRepr('301.0')
            ],
            [
                GenericRepr('246.0'),
                GenericRepr('289.0')
            ],
            [
                GenericRepr('259.0'),
                GenericRepr('367.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            290.0,
            166.0
        ],
        'pixel_corners': [
            [
                GenericRepr('241.0'),
                GenericRepr('259.0')
            ],
            [
                GenericRepr('136.0'),
                GenericRepr('270.0')
            ],
            [
                GenericRepr('139.0'),
                GenericRepr('216.0')
            ],
            [
                GenericRepr('237.0'),
                GenericRepr('207.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            400.0,
            553.0
        ],
        'pixel_corners': [
            [
                GenericRepr('351.0'),
                GenericRepr('522.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('525.0')
            ],
            [
                GenericRepr('474.0'),
                GenericRepr('603.0')
            ],
            [
                GenericRepr('358.0'),
                GenericRepr('604.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            523.0,
            360.0
        ],
        'pixel_corners': [
            [
                GenericRepr('474.0'),
                GenericRepr('489.0')
            ],
            [
                GenericRepr('354.0'),
                GenericRepr('487.0')
            ],
            [
                GenericRepr('365.0'),
                GenericRepr('410.0')
            ],
            [
                GenericRepr('478.0'),
                GenericRepr('413.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            659.0,
            302.0
        ],
        'pixel_corners': [
            [
                GenericRepr('610.0'),
                GenericRepr('262.0')
            ],
            [
                GenericRepr('703.0'),
                GenericRepr('277.0')
            ],
            [
                GenericRepr('697.0'),
                GenericRepr('352.0')
            ],
            [
                GenericRepr('608.0'),
                GenericRepr('337.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            756.0,
            139.0
        ],
        'pixel_corners': [
            [
                GenericRepr('707.0'),
                GenericRepr('250.0')
            ],
            [
                GenericRepr('615.0'),
                GenericRepr('236.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('189.0')
            ],
            [
                GenericRepr('723.0'),
                GenericRepr('202.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            1060.0,
            500.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1011.0'),
                GenericRepr('639.0')
            ],
            [
                GenericRepr('896.0'),
                GenericRepr('629.0')
            ],
            [
                GenericRepr('916.0'),
                GenericRepr('550.0')
            ],
            [
                GenericRepr('1037.0'),
                GenericRepr('560.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            1064.0,
            465.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1015.0'),
                GenericRepr('446.0')
            ],
            [
                GenericRepr('1034.0'),
                GenericRepr('528.0')
            ],
            [
                GenericRepr('913.0'),
                GenericRepr('515.0')
            ],
            [
                GenericRepr('902.0'),
                GenericRepr('436.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-202759.jpg] 1'] = [
    {
        'id': 54,
        'pixel_centre': [
            349.0,
            243.0
        ],
        'pixel_corners': [
            [
                GenericRepr('300.0'),
                GenericRepr('354.0')
            ],
            [
                GenericRepr('271.0'),
                GenericRepr('284.0')
            ],
            [
                GenericRepr('415.0'),
                GenericRepr('293.0')
            ],
            [
                GenericRepr('433.0'),
                GenericRepr('363.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            465.0,
            73.0
        ],
        'pixel_corners': [
            [
                GenericRepr('416.0'),
                GenericRepr('249.0')
            ],
            [
                GenericRepr('271.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('297.0'),
                GenericRepr('123.0')
            ],
            [
                GenericRepr('435.0'),
                GenericRepr('132.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            524.0,
            477.0
        ],
        'pixel_corners': [
            [
                GenericRepr('475.0'),
                GenericRepr('689.0')
            ],
            [
                GenericRepr('301.0'),
                GenericRepr('689.0')
            ],
            [
                GenericRepr('320.0'),
                GenericRepr('527.0')
            ],
            [
                GenericRepr('483.0'),
                GenericRepr('529.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            714.0,
            265.0
        ],
        'pixel_corners': [
            [
                GenericRepr('665.0'),
                GenericRepr('238.0')
            ],
            [
                GenericRepr('805.0'),
                GenericRepr('243.0')
            ],
            [
                GenericRepr('791.0'),
                GenericRepr('315.0')
            ],
            [
                GenericRepr('661.0'),
                GenericRepr('309.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            854.0,
            36.0
        ],
        'pixel_corners': [
            [
                GenericRepr('805.0'),
                GenericRepr('203.0')
            ],
            [
                GenericRepr('664.0'),
                GenericRepr('197.0')
            ],
            [
                GenericRepr('669.0'),
                GenericRepr('86.0')
            ],
            [
                GenericRepr('804.0'),
                GenericRepr('92.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            984.0,
            517.0
        ],
        'pixel_corners': [
            [
                GenericRepr('935.0'),
                GenericRepr('627.0')
            ],
            [
                GenericRepr('791.0'),
                GenericRepr('617.0')
            ],
            [
                GenericRepr('811.0'),
                GenericRepr('567.0')
            ],
            [
                GenericRepr('970.0'),
                GenericRepr('577.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            1009.0,
            474.0
        ],
        'pixel_corners': [
            [
                GenericRepr('960.0'),
                GenericRepr('392.0')
            ],
            [
                GenericRepr('969.0'),
                GenericRepr('536.0')
            ],
            [
                GenericRepr('808.0'),
                GenericRepr('524.0')
            ],
            [
                GenericRepr('807.0'),
                GenericRepr('382.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-202825.jpg] 1'] = [
    {
        'id': 52,
        'pixel_centre': [
            226.0,
            229.0
        ],
        'pixel_corners': [
            [
                GenericRepr('177.0'),
                GenericRepr('242.0')
            ],
            [
                GenericRepr('223.0'),
                GenericRepr('234.0')
            ],
            [
                GenericRepr('230.0'),
                GenericRepr('279.0')
            ],
            [
                GenericRepr('182.0'),
                GenericRepr('286.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            443.0,
            367.0
        ],
        'pixel_corners': [
            [
                GenericRepr('394.0'),
                GenericRepr('398.0')
            ],
            [
                GenericRepr('457.0'),
                GenericRepr('393.0')
            ],
            [
                GenericRepr('470.0'),
                GenericRepr('417.0')
            ],
            [
                GenericRepr('404.0'),
                GenericRepr('421.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            456.0,
            444.0
        ],
        'pixel_corners': [
            [
                GenericRepr('407.0'),
                GenericRepr('440.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('434.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('494.0')
            ],
            [
                GenericRepr('408.0'),
                GenericRepr('500.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            753.0,
            210.0
        ],
        'pixel_corners': [
            [
                GenericRepr('704.0'),
                GenericRepr('303.0')
            ],
            [
                GenericRepr('705.0'),
                GenericRepr('258.0')
            ],
            [
                GenericRepr('753.0'),
                GenericRepr('260.0')
            ],
            [
                GenericRepr('751.0'),
                GenericRepr('305.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            987.0,
            270.0
        ],
        'pixel_corners': [
            [
                GenericRepr('938.0'),
                GenericRepr('378.0')
            ],
            [
                GenericRepr('883.0'),
                GenericRepr('370.0')
            ],
            [
                GenericRepr('888.0'),
                GenericRepr('320.0')
            ],
            [
                GenericRepr('943.0'),
                GenericRepr('327.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203003.jpg] 1'] = [
    {
        'id': 45,
        'pixel_centre': [
            209.0,
            415.0
        ],
        'pixel_corners': [
            [
                GenericRepr('160.0'),
                GenericRepr('593.0')
            ],
            [
                GenericRepr('130.0'),
                GenericRepr('448.0')
            ],
            [
                GenericRepr('203.0'),
                GenericRepr('465.0')
            ],
            [
                GenericRepr('231.0'),
                GenericRepr('623.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            325.0,
            370.0
        ],
        'pixel_corners': [
            [
                GenericRepr('276.0'),
                GenericRepr('620.0')
            ],
            [
                GenericRepr('246.0'),
                GenericRepr('463.0')
            ],
            [
                GenericRepr('387.0'),
                GenericRepr('420.0')
            ],
            [
                GenericRepr('411.0'),
                GenericRepr('566.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            501.0,
            26.0
        ],
        'pixel_corners': [
            [
                GenericRepr('452.0'),
                GenericRepr('172.0')
            ],
            [
                GenericRepr('423.0'),
                GenericRepr('96.0')
            ],
            [
                GenericRepr('539.0'),
                GenericRepr('76.0')
            ],
            [
                GenericRepr('573.0'),
                GenericRepr('150.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            921.0,
            268.0
        ],
        'pixel_corners': [
            [
                GenericRepr('872.0'),
                GenericRepr('469.0')
            ],
            [
                GenericRepr('859.0'),
                GenericRepr('332.0')
            ],
            [
                GenericRepr('1006.0'),
                GenericRepr('318.0')
            ],
            [
                GenericRepr('1016.0'),
                GenericRepr('458.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203035.jpg] 1'] = [
    {
        'id': 60,
        'pixel_centre': [
            335.0,
            100.0
        ],
        'pixel_corners': [
            [
                GenericRepr('286.0'),
                GenericRepr('228.0')
            ],
            [
                GenericRepr('320.0'),
                GenericRepr('165.0')
            ],
            [
                GenericRepr('441.0'),
                GenericRepr('150.0')
            ],
            [
                GenericRepr('414.0'),
                GenericRepr('214.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            372.0,
            198.0
        ],
        'pixel_corners': [
            [
                GenericRepr('323.0'),
                GenericRepr('373.0')
            ],
            [
                GenericRepr('284.0'),
                GenericRepr('262.0')
            ],
            [
                GenericRepr('416.0'),
                GenericRepr('248.0')
            ],
            [
                GenericRepr('448.0'),
                GenericRepr('363.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            503.0,
            222.0
        ],
        'pixel_corners': [
            [
                GenericRepr('454.0'),
                GenericRepr('233.0')
            ],
            [
                GenericRepr('476.0'),
                GenericRepr('166.0')
            ],
            [
                GenericRepr('504.0'),
                GenericRepr('272.0')
            ],
            [
                GenericRepr('485.0'),
                GenericRepr('342.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            508.0,
            484.0
        ],
        'pixel_corners': [
            [
                GenericRepr('459.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('495.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('500.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('465.0'),
                GenericRepr('546.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            602.0,
            345.0
        ],
        'pixel_corners': [
            [
                GenericRepr('553.0'),
                GenericRepr('582.0')
            ],
            [
                GenericRepr('549.0'),
                GenericRepr('403.0')
            ],
            [
                GenericRepr('705.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('710.0'),
                GenericRepr('587.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            810.0,
            517.0
        ],
        'pixel_corners': [
            [
                GenericRepr('761.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('837.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('844.0'),
                GenericRepr('567.0')
            ],
            [
                GenericRepr('768.0'),
                GenericRepr('586.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203112.jpg] 1'] = [
    {
        'id': 45,
        'pixel_centre': [
            534.0,
            340.0
        ],
        'pixel_corners': [
            [
                GenericRepr('485.0'),
                GenericRepr('426.0')
            ],
            [
                GenericRepr('443.0'),
                GenericRepr('430.0')
            ],
            [
                GenericRepr('442.0'),
                GenericRepr('390.0')
            ],
            [
                GenericRepr('484.0'),
                GenericRepr('386.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            683.0,
            355.0
        ],
        'pixel_corners': [
            [
                GenericRepr('634.0'),
                GenericRepr('368.0')
            ],
            [
                GenericRepr('673.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('675.0'),
                GenericRepr('405.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('407.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            875.0,
            356.0
        ],
        'pixel_corners': [
            [
                GenericRepr('826.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('825.0'),
                GenericRepr('404.0')
            ],
            [
                GenericRepr('786.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('787.0'),
                GenericRepr('368.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            1016.0,
            361.0
        ],
        'pixel_corners': [
            [
                GenericRepr('967.0'),
                GenericRepr('379.0')
            ],
            [
                GenericRepr('965.0'),
                GenericRepr('419.0')
            ],
            [
                GenericRepr('929.0'),
                GenericRepr('411.0')
            ],
            [
                GenericRepr('931.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            1027.0,
            321.0
        ],
        'pixel_corners': [
            [
                GenericRepr('978.0'),
                GenericRepr('419.0')
            ],
            [
                GenericRepr('980.0'),
                GenericRepr('380.0')
            ],
            [
                GenericRepr('1001.0'),
                GenericRepr('371.0')
            ],
            [
                GenericRepr('999.0'),
                GenericRepr('409.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203132.jpg] 1'] = [
    {
        'id': 52,
        'pixel_centre': [
            649.0,
            294.0
        ],
        'pixel_corners': [
            [
                GenericRepr('600.0'),
                GenericRepr('311.0')
            ],
            [
                GenericRepr('634.0'),
                GenericRepr('310.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('344.0')
            ],
            [
                GenericRepr('601.0'),
                GenericRepr('345.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            813.0,
            295.0
        ],
        'pixel_corners': [
            [
                GenericRepr('764.0'),
                GenericRepr('310.0')
            ],
            [
                GenericRepr('765.0'),
                GenericRepr('344.0')
            ],
            [
                GenericRepr('731.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('730.0'),
                GenericRepr('311.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            926.0,
            295.0
        ],
        'pixel_corners': [
            [
                GenericRepr('877.0'),
                GenericRepr('308.0')
            ],
            [
                GenericRepr('878.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('852.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('852.0'),
                GenericRepr('309.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            938.0,
            259.0
        ],
        'pixel_corners': [
            [
                GenericRepr('889.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('889.0'),
                GenericRepr('309.0')
            ],
            [
                GenericRepr('915.0'),
                GenericRepr('309.0')
            ],
            [
                GenericRepr('915.0'),
                GenericRepr('345.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203401.jpg] 1'] = [
    {
        'id': 54,
        'pixel_centre': [
            161.0,
            156.0
        ],
        'pixel_corners': [
            [
                GenericRepr('112.0'),
                GenericRepr('343.0')
            ],
            [
                GenericRepr('110.0'),
                GenericRepr('216.0')
            ],
            [
                GenericRepr('175.0'),
                GenericRepr('206.0')
            ],
            [
                GenericRepr('179.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            269.0,
            167.0
        ],
        'pixel_corners': [
            [
                GenericRepr('220.0'),
                GenericRepr('342.0')
            ],
            [
                GenericRepr('217.0'),
                GenericRepr('209.0')
            ],
            [
                GenericRepr('329.0'),
                GenericRepr('217.0')
            ],
            [
                GenericRepr('332.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            768.0,
            288.0
        ],
        'pixel_corners': [
            [
                GenericRepr('719.0'),
                GenericRepr('237.0')
            ],
            [
                GenericRepr('721.0'),
                GenericRepr('339.0')
            ],
            [
                GenericRepr('673.0'),
                GenericRepr('338.0')
            ],
            [
                GenericRepr('671.0'),
                GenericRepr('244.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            798.0,
            289.0
        ],
        'pixel_corners': [
            [
                GenericRepr('749.0'),
                GenericRepr('238.0')
            ],
            [
                GenericRepr('834.0'),
                GenericRepr('240.0')
            ],
            [
                GenericRepr('833.0'),
                GenericRepr('339.0')
            ],
            [
                GenericRepr('750.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            968.0,
            288.0
        ],
        'pixel_corners': [
            [
                GenericRepr('919.0'),
                GenericRepr('244.0')
            ],
            [
                GenericRepr('1007.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('1007.0'),
                GenericRepr('338.0')
            ],
            [
                GenericRepr('920.0'),
                GenericRepr('338.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            1084.0,
            193.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1035.0'),
                GenericRepr('337.0')
            ],
            [
                GenericRepr('1038.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('1078.0'),
                GenericRepr('243.0')
            ],
            [
                GenericRepr('1075.0'),
                GenericRepr('337.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203608.jpg] 1'] = [
    {
        'id': 45,
        'pixel_centre': [
            691.0,
            327.0
        ],
        'pixel_corners': [
            [
                GenericRepr('642.0'),
                GenericRepr('527.0')
            ],
            [
                GenericRepr('494.0'),
                GenericRepr('525.0')
            ],
            [
                GenericRepr('497.0'),
                GenericRepr('377.0')
            ],
            [
                GenericRepr('643.0'),
                GenericRepr('381.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203623.jpg] 1'] = [
    {
        'id': 52,
        'pixel_centre': [
            1251.0,
            482.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1202.0'),
                GenericRepr('355.0')
            ],
            [
                GenericRepr('1211.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('1111.0'),
                GenericRepr('532.0')
            ],
            [
                GenericRepr('1104.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203643.jpg] 1'] = [
    {
        'id': 52,
        'pixel_centre': [
            1252.0,
            482.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1203.0'),
                GenericRepr('355.0')
            ],
            [
                GenericRepr('1211.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('1111.0'),
                GenericRepr('532.0')
            ],
            [
                GenericRepr('1104.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203703.jpg] 1'] = [
    {
        'id': 54,
        'pixel_centre': [
            509.0,
            315.0
        ],
        'pixel_corners': [
            [
                GenericRepr('460.0'),
                GenericRepr('519.0')
            ],
            [
                GenericRepr('464.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('616.0'),
                GenericRepr('365.0')
            ],
            [
                GenericRepr('615.0'),
                GenericRepr('521.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            1136.0,
            325.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1087.0'),
                GenericRepr('531.0')
            ],
            [
                GenericRepr('928.0'),
                GenericRepr('528.0')
            ],
            [
                GenericRepr('926.0'),
                GenericRepr('375.0')
            ],
            [
                GenericRepr('1083.0'),
                GenericRepr('376.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers[2019-06-08-203821.jpg] 1'] = [
    {
        'id': 54,
        'pixel_centre': [
            191.0,
            309.0
        ],
        'pixel_corners': [
            [
                GenericRepr('142.0'),
                GenericRepr('493.0')
            ],
            [
                GenericRepr('144.0'),
                GenericRepr('374.0')
            ],
            [
                GenericRepr('183.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('181.0'),
                GenericRepr('489.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 54,
        'pixel_centre': [
            270.0,
            316.0
        ],
        'pixel_corners': [
            [
                GenericRepr('221.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('222.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('344.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('344.0'),
                GenericRepr('488.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 45,
        'pixel_centre': [
            736.0,
            326.0
        ],
        'pixel_corners': [
            [
                GenericRepr('687.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('579.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('579.0'),
                GenericRepr('376.0')
            ],
            [
                GenericRepr('688.0'),
                GenericRepr('379.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 60,
        'pixel_centre': [
            884.0,
            325.0
        ],
        'pixel_corners': [
            [
                GenericRepr('835.0'),
                GenericRepr('492.0')
            ],
            [
                GenericRepr('833.0'),
                GenericRepr('377.0')
            ],
            [
                GenericRepr('948.0'),
                GenericRepr('375.0')
            ],
            [
                GenericRepr('952.0'),
                GenericRepr('493.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            1159.0,
            440.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1110.0'),
                GenericRepr('362.0')
            ],
            [
                GenericRepr('1116.0'),
                GenericRepr('491.0')
            ],
            [
                GenericRepr('1042.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('1037.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100
    },
    {
        'id': 52,
        'pixel_centre': [
            1201.0,
            444.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1152.0'),
                GenericRepr('363.0')
            ],
            [
                GenericRepr('1260.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('1263.0'),
                GenericRepr('494.0')
            ],
            [
                GenericRepr('1155.0'),
                GenericRepr('493.0')
            ]
        ],
        'size': 100
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-202719.jpg-C270] 1'] = [
    {
        'cartesian': [
            48.97247358170491,
            -43.540491875278086,
            2267.382873156615
        ],
        'distance': 2268,
        'id': 54,
        'orientation': (
            -2.374775138098944,
            -0.009807428993270965,
            1.7362260197255788
        ),
        'pixel_centre': [
            207.0,
            239.0
        ],
        'pixel_corners': [
            [
                GenericRepr('158.0'),
                GenericRepr('379.0')
            ],
            [
                GenericRepr('139.0'),
                GenericRepr('301.0')
            ],
            [
                GenericRepr('246.0'),
                GenericRepr('289.0')
            ],
            [
                GenericRepr('259.0'),
                GenericRepr('367.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.019200613033588776,
            0.02159532076609588,
            2268
        )
    },
    {
        'cartesian': [
            38.621549153972964,
            -137.80162512034136,
            2333.0145288597682
        ],
        'distance': 2337,
        'id': 54,
        'orientation': (
            2.1605344813034515,
            -0.12187790230224262,
            3.130920068765706
        ),
        'pixel_centre': [
            290.0,
            166.0
        ],
        'pixel_corners': [
            [
                GenericRepr('241.0'),
                GenericRepr('259.0')
            ],
            [
                GenericRepr('136.0'),
                GenericRepr('270.0')
            ],
            [
                GenericRepr('139.0'),
                GenericRepr('216.0')
            ],
            [
                GenericRepr('237.0'),
                GenericRepr('207.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.05899736361515225,
            0.016552842350917953,
            2337
        )
    },
    {
        'cartesian': [
            225.15552374510497,
            149.15209372976605,
            2058.5813186709834
        ],
        'distance': 2076,
        'id': 52,
        'orientation': (
            -2.340785501297267,
            -0.07367321031068015,
            0.10059263412692815
        ),
        'pixel_centre': [
            400.0,
            553.0
        ],
        'pixel_corners': [
            [
                GenericRepr('351.0'),
                GenericRepr('522.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('525.0')
            ],
            [
                GenericRepr('474.0'),
                GenericRepr('603.0')
            ],
            [
                GenericRepr('358.0'),
                GenericRepr('604.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.07232744086108522,
            0.10894108910495433,
            2076
        )
    },
    {
        'cartesian': [
            232.6617149320773,
            55.539256082026675,
            2084.684736553089
        ],
        'distance': 2098,
        'id': 52,
        'orientation': (
            2.2310366500853216,
            -0.12512995161344634,
            2.980443908823364
        ),
        'pixel_centre': [
            523.0,
            360.0
        ],
        'pixel_corners': [
            [
                GenericRepr('474.0'),
                GenericRepr('489.0')
            ],
            [
                GenericRepr('354.0'),
                GenericRepr('487.0')
            ],
            [
                GenericRepr('365.0'),
                GenericRepr('410.0')
            ],
            [
                GenericRepr('478.0'),
                GenericRepr('413.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.026635260774595937,
            0.11114528555036168,
            2098
        )
    },
    {
        'cartesian': [
            579.2978057029335,
            -88.94695650886655,
            2770.9294952039127
        ],
        'distance': 2832,
        'id': 60,
        'orientation': (
            -2.511251547498965,
            -0.38631806341066616,
            0.06936643203800477
        ),
        'pixel_centre': [
            659.0,
            302.0
        ],
        'pixel_corners': [
            [
                GenericRepr('610.0'),
                GenericRepr('262.0')
            ],
            [
                GenericRepr('703.0'),
                GenericRepr('277.0')
            ],
            [
                GenericRepr('697.0'),
                GenericRepr('352.0')
            ],
            [
                GenericRepr('608.0'),
                GenericRepr('337.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.032089024583045085,
            0.2060942464482809,
            2832
        )
    },
    {
        'cartesian': [
            618.1004750940332,
            -194.6624239721691,
            2869.457529588602
        ],
        'distance': 2941,
        'id': 60,
        'orientation': (
            2.2425686591916687,
            -0.05607015160098767,
            2.780934796976062
        ),
        'pixel_centre': [
            756.0,
            139.0
        ],
        'pixel_corners': [
            [
                GenericRepr('707.0'),
                GenericRepr('250.0')
            ],
            [
                GenericRepr('615.0'),
                GenericRepr('236.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('189.0')
            ],
            [
                GenericRepr('723.0'),
                GenericRepr('202.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.06773566756178286,
            0.21216489101779432,
            2941
        )
    },
    {
        'cartesian': [
            940.1588374368113,
            224.43899142207056,
            3108.420708301315
        ],
        'distance': 3255,
        'id': 45,
        'orientation': (
            -2.6905576238675173,
            0.35601013314439545,
            2.9899714705455573
        ),
        'pixel_centre': [
            1060.0,
            500.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1011.0'),
                GenericRepr('639.0')
            ],
            [
                GenericRepr('896.0'),
                GenericRepr('629.0')
            ],
            [
                GenericRepr('916.0'),
                GenericRepr('550.0')
            ],
            [
                GenericRepr('1037.0'),
                GenericRepr('560.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.07207846088374699,
            0.29370799143453274,
            3255
        )
    },
    {
        'cartesian': [
            1049.5881203039353,
            108.63429004043235,
            3428.3895118517153
        ],
        'distance': 3587,
        'id': 45,
        'orientation': (
            2.9291313262640166,
            0.2475668396986916,
            -1.5803413376036526
        ),
        'pixel_centre': [
            1064.0,
            465.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1015.0'),
                GenericRepr('446.0')
            ],
            [
                GenericRepr('1034.0'),
                GenericRepr('528.0')
            ],
            [
                GenericRepr('913.0'),
                GenericRepr('515.0')
            ],
            [
                GenericRepr('902.0'),
                GenericRepr('436.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.031676083950300755,
            0.2970858479527087,
            3587
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-202759.jpg-C270] 1'] = [
    {
        'cartesian': [
            145.74373036840615,
            -40.256101048113365,
            1695.8865525211438
        ],
        'distance': 1702,
        'id': 54,
        'orientation': (
            -2.021155971629812,
            -0.1928500018914251,
            1.813522035967637
        ),
        'pixel_centre': [
            349.0,
            243.0
        ],
        'pixel_corners': [
            [
                GenericRepr('300.0'),
                GenericRepr('354.0')
            ],
            [
                GenericRepr('271.0'),
                GenericRepr('284.0')
            ],
            [
                GenericRepr('415.0'),
                GenericRepr('293.0')
            ],
            [
                GenericRepr('433.0'),
                GenericRepr('363.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.023733039527514883,
            0.08572891261099974,
            1702
        )
    },
    {
        'cartesian': [
            143.68573293688746,
            -134.99106597506574,
            1665.9077085539982
        ],
        'distance': 1677,
        'id': 54,
        'orientation': (
            2.5642693646694017,
            -0.17430626778660732,
            2.932965520289589
        ),
        'pixel_centre': [
            465.0,
            73.0
        ],
        'pixel_corners': [
            [
                GenericRepr('416.0'),
                GenericRepr('249.0')
            ],
            [
                GenericRepr('271.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('297.0'),
                GenericRepr('123.0')
            ],
            [
                GenericRepr('435.0'),
                GenericRepr('132.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.08085488075673547,
            0.08603778740109605,
            1677
        )
    },
    {
        'cartesian': [
            142.89344515411798,
            126.15052127191359,
            1416.1887644677813
        ],
        'distance': 1428,
        'id': 52,
        'orientation': (
            2.5408392198729035,
            -0.2964381644472136,
            2.9899950612903115
        ),
        'pixel_centre': [
            524.0,
            477.0
        ],
        'pixel_corners': [
            [
                GenericRepr('475.0'),
                GenericRepr('689.0')
            ],
            [
                GenericRepr('301.0'),
                GenericRepr('689.0')
            ],
            [
                GenericRepr('320.0'),
                GenericRepr('527.0')
            ],
            [
                GenericRepr('483.0'),
                GenericRepr('529.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.08884298789037894,
            0.10055966114207664,
            1428
        )
    },
    {
        'cartesian': [
            495.37653019908004,
            -92.71839331607553,
            2086.756057805681
        ],
        'distance': 2146,
        'id': 60,
        'orientation': (
            -2.146688086504218,
            -0.15376856564237784,
            0.13250201533075248
        ),
        'pixel_centre': [
            714.0,
            265.0
        ],
        'pixel_corners': [
            [
                GenericRepr('665.0'),
                GenericRepr('238.0')
            ],
            [
                GenericRepr('805.0'),
                GenericRepr('243.0')
            ],
            [
                GenericRepr('791.0'),
                GenericRepr('315.0')
            ],
            [
                GenericRepr('661.0'),
                GenericRepr('309.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.04440262705270071,
            0.2330763563068217,
            2146
        )
    },
    {
        'cartesian': [
            485.8525286176275,
            -197.6108472448464,
            2040.2058111030517
        ],
        'distance': 2106,
        'id': 60,
        'orientation': (
            2.7450103543587057,
            0.08918522900956188,
            3.0779710073436153
        ),
        'pixel_centre': [
            854.0,
            36.0
        ],
        'pixel_corners': [
            [
                GenericRepr('805.0'),
                GenericRepr('203.0')
            ],
            [
                GenericRepr('664.0'),
                GenericRepr('197.0')
            ],
            [
                GenericRepr('669.0'),
                GenericRepr('86.0')
            ],
            [
                GenericRepr('804.0'),
                GenericRepr('92.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.09655709123623162,
            0.23378457466325744,
            2106
        )
    },
    {
        'cartesian': [
            673.6284363791592,
            183.85764494825509,
            2410.542678086448
        ],
        'distance': 2509,
        'id': 45,
        'orientation': (
            1.8840792107646445,
            -0.2865274976792751,
            2.6473169753369916
        ),
        'pixel_centre': [
            984.0,
            517.0
        ],
        'pixel_corners': [
            [
                GenericRepr('935.0'),
                GenericRepr('627.0')
            ],
            [
                GenericRepr('791.0'),
                GenericRepr('617.0')
            ],
            [
                GenericRepr('811.0'),
                GenericRepr('567.0')
            ],
            [
                GenericRepr('970.0'),
                GenericRepr('577.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.0761249147287415,
            0.2724994947028334,
            2509
        )
    },
    {
        'cartesian': [
            534.5034319853727,
            46.41496320872599,
            1871.284594446041
        ],
        'distance': 1946,
        'id': 45,
        'orientation': (
            3.1288802071645088,
            0.41829537250197435,
            -1.6007313539829524
        ),
        'pixel_centre': [
            1009.0,
            474.0
        ],
        'pixel_corners': [
            [
                GenericRepr('960.0'),
                GenericRepr('392.0')
            ],
            [
                GenericRepr('969.0'),
                GenericRepr('536.0')
            ],
            [
                GenericRepr('808.0'),
                GenericRepr('524.0')
            ],
            [
                GenericRepr('807.0'),
                GenericRepr('382.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.024798712209911596,
            0.2782258895906213,
            1946
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-202825.jpg-C270] 1'] = [
    {
        'cartesian': [
            113.50031115128753,
            -248.6544685541128,
            4995.715426354672
        ],
        'distance': 5003,
        'id': 52,
        'orientation': (
            2.8020065399053813,
            -0.1341033851011886,
            0.1159768707354907
        ),
        'pixel_centre': [
            226.0,
            229.0
        ],
        'pixel_corners': [
            [
                GenericRepr('177.0'),
                GenericRepr('242.0')
            ],
            [
                GenericRepr('223.0'),
                GenericRepr('234.0')
            ],
            [
                GenericRepr('230.0'),
                GenericRepr('279.0')
            ],
            [
                GenericRepr('182.0'),
                GenericRepr('286.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.0497325032941344,
            0.022715623040754706,
            5003
        )
    },
    {
        'cartesian': [
            437.14331427744634,
            36.11418563006483,
            3719.93984313552
        ],
        'distance': 3745,
        'id': 45,
        'orientation': (
            1.9246362915541546,
            -0.06308216454554283,
            0.0619012595336596
        ),
        'pixel_centre': [
            443.0,
            367.0
        ],
        'pixel_corners': [
            [
                GenericRepr('394.0'),
                GenericRepr('398.0')
            ],
            [
                GenericRepr('457.0'),
                GenericRepr('393.0')
            ],
            [
                GenericRepr('470.0'),
                GenericRepr('417.0')
            ],
            [
                GenericRepr('404.0'),
                GenericRepr('421.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.009707966425076632,
            0.11697705039027918,
            3745
        )
    },
    {
        'cartesian': [
            438.9721413021396,
            122.79979847441793,
            3630.597292416694
        ],
        'distance': 3659,
        'id': 45,
        'orientation': (
            -2.672136565431361,
            0.12379183782061447,
            0.04930034366911938
        ),
        'pixel_centre': [
            456.0,
            444.0
        ],
        'pixel_corners': [
            [
                GenericRepr('407.0'),
                GenericRepr('440.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('434.0')
            ],
            [
                GenericRepr('473.0'),
                GenericRepr('494.0')
            ],
            [
                GenericRepr('408.0'),
                GenericRepr('500.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.033810690537705065,
            0.12032499440047467,
            3659
        )
    },
    {
        'cartesian': [
            1319.4297482330408,
            -237.21862472588327,
            5549.346373593318
        ],
        'distance': 5708,
        'id': 60,
        'orientation': (
            3.130901978771658,
            0.1033472544638747,
            1.5343295620823738
        ),
        'pixel_centre': [
            753.0,
            210.0
        ],
        'pixel_corners': [
            [
                GenericRepr('704.0'),
                GenericRepr('303.0')
            ],
            [
                GenericRepr('705.0'),
                GenericRepr('258.0')
            ],
            [
                GenericRepr('753.0'),
                GenericRepr('260.0')
            ],
            [
                GenericRepr('751.0'),
                GenericRepr('305.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.04272111988817821,
            0.23342882954994468,
            5708
        )
    },
    {
        'cartesian': [
            1539.1078609047545,
            -85.75371591622213,
            5206.422170013941
        ],
        'distance': 5429,
        'id': 54,
        'orientation': (
            3.0847199591610925,
            0.5060232477609161,
            3.028944535387404
        ),
        'pixel_centre': [
            987.0,
            270.0
        ],
        'pixel_corners': [
            [
                GenericRepr('938.0'),
                GenericRepr('378.0')
            ],
            [
                GenericRepr('883.0'),
                GenericRepr('370.0')
            ],
            [
                GenericRepr('888.0'),
                GenericRepr('320.0')
            ],
            [
                GenericRepr('943.0'),
                GenericRepr('327.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.01646926810550821,
            0.2874310279409345,
            5429
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203003.jpg-C270] 1'] = [
    {
        'cartesian': [
            20.48851199982102,
            95.69566069733483,
            1580.5788190031387
        ],
        'distance': 1583,
        'id': 45,
        'orientation': (
            -2.5848888249788726,
            -1.0496249961048107,
            1.9683197477307306
        ),
        'pixel_centre': [
            209.0,
            415.0
        ],
        'pixel_corners': [
            [
                GenericRepr('160.0'),
                GenericRepr('593.0')
            ],
            [
                GenericRepr('130.0'),
                GenericRepr('448.0')
            ],
            [
                GenericRepr('203.0'),
                GenericRepr('465.0')
            ],
            [
                GenericRepr('231.0'),
                GenericRepr('623.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.06047087737739141,
            0.012961937932580238,
            1583
        )
    },
    {
        'cartesian': [
            115.09648190599003,
            82.89109754682602,
            1525.4457324445514
        ],
        'distance': 1532,
        'id': 45,
        'orientation': (
            -2.9060264302941743,
            0.4133142759398382,
            1.7714497542688457
        ),
        'pixel_centre': [
            325.0,
            370.0
        ],
        'pixel_corners': [
            [
                GenericRepr('276.0'),
                GenericRepr('620.0')
            ],
            [
                GenericRepr('246.0'),
                GenericRepr('463.0')
            ],
            [
                GenericRepr('387.0'),
                GenericRepr('420.0')
            ],
            [
                GenericRepr('411.0'),
                GenericRepr('566.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.05428554768457168,
            0.07530835941656067,
            1532
        )
    },
    {
        'cartesian': [
            289.91616050097764,
            -212.77135366250374,
            1991.8391295376969
        ],
        'distance': 2024,
        'id': 60,
        'orientation': (
            2.3558760516232677,
            -0.10217370213786375,
            1.7257551854534197
        ),
        'pixel_centre': [
            501.0,
            26.0
        ],
        'pixel_corners': [
            [
                GenericRepr('452.0'),
                GenericRepr('172.0')
            ],
            [
                GenericRepr('423.0'),
                GenericRepr('96.0')
            ],
            [
                GenericRepr('539.0'),
                GenericRepr('76.0')
            ],
            [
                GenericRepr('573.0'),
                GenericRepr('150.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.10641800652759896,
            0.14453700829579358,
            2024
        )
    },
    {
        'cartesian': [
            583.5382492994955,
            0.8816396212834946,
            1943.5842622796292
        ],
        'distance': 2029,
        'id': 54,
        'orientation': (
            -3.080013487331484,
            0.5672894694515732,
            1.6484831876888573
        ),
        'pixel_centre': [
            921.0,
            268.0
        ],
        'pixel_corners': [
            [
                GenericRepr('872.0'),
                GenericRepr('469.0')
            ],
            [
                GenericRepr('859.0'),
                GenericRepr('332.0')
            ],
            [
                GenericRepr('1006.0'),
                GenericRepr('318.0')
            ],
            [
                GenericRepr('1016.0'),
                GenericRepr('458.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.00045361530133953935,
            0.29167531643278244,
            2029
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203035.jpg-C270] 1'] = [
    {
        'cartesian': [
            164.77687930600482,
            -144.46545080882265,
            1817.7412559756758
        ],
        'distance': 1830,
        'id': 60,
        'orientation': (
            2.07661357474768,
            -0.2871784941821913,
            1.2467481609809512
        ),
        'pixel_centre': [
            335.0,
            100.0
        ],
        'pixel_corners': [
            [
                GenericRepr('286.0'),
                GenericRepr('228.0')
            ],
            [
                GenericRepr('320.0'),
                GenericRepr('165.0')
            ],
            [
                GenericRepr('441.0'),
                GenericRepr('150.0')
            ],
            [
                GenericRepr('414.0'),
                GenericRepr('214.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.07930855654857982,
            0.09040216887952719,
            1830
        )
    },
    {
        'cartesian': [
            161.4722561665811,
            -50.73479763501068,
            1768.2769166205892
        ],
        'distance': 1776,
        'id': 60,
        'orientation': (
            -2.47467891707711,
            -0.2870130010351253,
            1.8918627704858753
        ),
        'pixel_centre': [
            372.0,
            198.0
        ],
        'pixel_corners': [
            [
                GenericRepr('323.0'),
                GenericRepr('373.0')
            ],
            [
                GenericRepr('284.0'),
                GenericRepr('262.0')
            ],
            [
                GenericRepr('416.0'),
                GenericRepr('248.0')
            ],
            [
                GenericRepr('448.0'),
                GenericRepr('363.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.02868378940620112,
            0.09106360388030527,
            1776
        )
    },
    {
        'cartesian': [
            264.2288895455216,
            -101.68069930155195,
            1908.5136086971556
        ],
        'distance': 1929,
        'id': 60,
        'orientation': (
            2.9194815679237767,
            1.1567369967876822,
            0.8230141052240988
        ),
        'pixel_centre': [
            503.0,
            222.0
        ],
        'pixel_corners': [
            [
                GenericRepr('454.0'),
                GenericRepr('233.0')
            ],
            [
                GenericRepr('476.0'),
                GenericRepr('166.0')
            ],
            [
                GenericRepr('504.0'),
                GenericRepr('272.0')
            ],
            [
                GenericRepr('485.0'),
                GenericRepr('342.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.05322710615864915,
            0.1375729372306014,
            1929
        )
    },
    {
        'cartesian': [
            256.23826211599015,
            66.70634334627935,
            1866.8194079498799
        ],
        'distance': 1885,
        'id': 52,
        'orientation': (
            3.089916374673172,
            1.1600914467598487,
            0.06401960891380874
        ),
        'pixel_centre': [
            508.0,
            484.0
        ],
        'pixel_corners': [
            [
                GenericRepr('459.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('495.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('500.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('465.0'),
                GenericRepr('546.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.03571742083320784,
            0.13640688796818903,
            1885
        )
    },
    {
        'cartesian': [
            267.83153094388206,
            56.58993306294073,
            1364.5048481694275
        ],
        'distance': 1391,
        'id': 54,
        'orientation': (
            2.9931084840564655,
            -0.784745976343979,
            1.5286223252515483
        ),
        'pixel_centre': [
            602.0,
            345.0
        ],
        'pixel_corners': [
            [
                GenericRepr('553.0'),
                GenericRepr('582.0')
            ],
            [
                GenericRepr('549.0'),
                GenericRepr('403.0')
            ],
            [
                GenericRepr('705.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('710.0'),
                GenericRepr('587.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.041449117388438136,
            0.19382069191808782,
            1391
        )
    },
    {
        'cartesian': [
            374.23985428691486,
            52.46482598758089,
            1430.589614052576
        ],
        'distance': 1479,
        'id': 54,
        'orientation': (
            -3.0833799621112803,
            0.964853309201618,
            -0.0040733153394813286
        ),
        'pixel_centre': [
            810.0,
            517.0
        ],
        'pixel_corners': [
            [
                GenericRepr('761.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('837.0'),
                GenericRepr('395.0')
            ],
            [
                GenericRepr('844.0'),
                GenericRepr('567.0')
            ],
            [
                GenericRepr('768.0'),
                GenericRepr('586.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.03665714022261602,
            0.2558645995142081,
            1479
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203112.jpg-C270] 1'] = [
    {
        'cartesian': [
            739.0535497132768,
            55.98058016808598,
            5648.073707934236
        ],
        'distance': 5696,
        'id': 45,
        'orientation': (
            -2.742018530298092,
            0.12260529728945267,
            -3.079420435154583
        ),
        'pixel_centre': [
            534.0,
            340.0
        ],
        'pixel_corners': [
            [
                GenericRepr('485.0'),
                GenericRepr('426.0')
            ],
            [
                GenericRepr('443.0'),
                GenericRepr('430.0')
            ],
            [
                GenericRepr('442.0'),
                GenericRepr('390.0')
            ],
            [
                GenericRepr('484.0'),
                GenericRepr('386.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.009911121924691738,
            0.1301113272642795,
            5696
        )
    },
    {
        'cartesian': [
            1306.1800442841482,
            -1.2842532389681658,
            6257.381731580902
        ],
        'distance': 6392,
        'id': 52,
        'orientation': (
            2.9216787995329607,
            -0.47615646393344757,
            -0.029168877915175397
        ),
        'pixel_centre': [
            683.0,
            355.0
        ],
        'pixel_corners': [
            [
                GenericRepr('634.0'),
                GenericRepr('368.0')
            ],
            [
                GenericRepr('673.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('675.0'),
                GenericRepr('405.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('407.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.00020523811332374002,
            0.20578727969670024,
            6392
        )
    },
    {
        'cartesian': [
            1750.2757816336425,
            -11.22994181322708,
            6616.916317181946
        ],
        'distance': 6844,
        'id': 60,
        'orientation': (
            -2.956769882623342,
            0.3613927869046201,
            -1.562310930346238
        ),
        'pixel_centre': [
            875.0,
            356.0
        ],
        'pixel_corners': [
            [
                GenericRepr('826.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('825.0'),
                GenericRepr('404.0')
            ],
            [
                GenericRepr('786.0'),
                GenericRepr('406.0')
            ],
            [
                GenericRepr('787.0'),
                GenericRepr('368.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.0016971547610582774,
            0.2585928057281205,
            6844
        )
    },
    {
        'cartesian': [
            2052.310983638644,
            4.816825291705704,
            6747.310697435263
        ],
        'distance': 7052,
        'id': 54,
        'orientation': (
            3.071969336115055,
            0.7015455718209448,
            -1.6967004469974478
        ),
        'pixel_centre': [
            1016.0,
            361.0
        ],
        'pixel_corners': [
            [
                GenericRepr('967.0'),
                GenericRepr('379.0')
            ],
            [
                GenericRepr('965.0'),
                GenericRepr('419.0')
            ],
            [
                GenericRepr('929.0'),
                GenericRepr('411.0')
            ],
            [
                GenericRepr('931.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.0007138880495395767,
            0.2952755670543514,
            7052
        )
    },
    {
        'cartesian': [
            2165.8879753672495,
            1.8969081407824882,
            6909.813197168766
        ],
        'distance': 7241,
        'id': 54,
        'orientation': (
            1.382196065375173,
            -1.4477970625090455,
            0.06103582713672187
        ),
        'pixel_centre': [
            1027.0,
            321.0
        ],
        'pixel_corners': [
            [
                GenericRepr('978.0'),
                GenericRepr('419.0')
            ],
            [
                GenericRepr('980.0'),
                GenericRepr('380.0')
            ],
            [
                GenericRepr('1001.0'),
                GenericRepr('371.0')
            ],
            [
                GenericRepr('999.0'),
                GenericRepr('409.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.0002745237879813167,
            0.303751040775963,
            7241
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203132.jpg-C270] 1'] = [
    {
        'cartesian': [
            1402.321068606438,
            -170.8835226211283,
            7210.4523971705175
        ],
        'distance': 7347,
        'id': 52,
        'orientation': (
            -3.0002956773507803,
            0.038872548559657924,
            0.04110850629582092
        ),
        'pixel_centre': [
            649.0,
            294.0
        ],
        'pixel_corners': [
            [
                GenericRepr('600.0'),
                GenericRepr('311.0')
            ],
            [
                GenericRepr('634.0'),
                GenericRepr('310.0')
            ],
            [
                GenericRepr('635.0'),
                GenericRepr('344.0')
            ],
            [
                GenericRepr('601.0'),
                GenericRepr('345.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.023694982095134886,
            0.19208659176797196,
            7347
        )
    },
    {
        'cartesian': [
            1807.8840602046369,
            -180.57348228893426,
            7386.732183680077
        ],
        'distance': 7606,
        'id': 60,
        'orientation': (
            -3.0906780369789457,
            0.2556989107409489,
            -1.5382122335842452
        ),
        'pixel_centre': [
            813.0,
            295.0
        ],
        'pixel_corners': [
            [
                GenericRepr('764.0'),
                GenericRepr('310.0')
            ],
            [
                GenericRepr('765.0'),
                GenericRepr('344.0')
            ],
            [
                GenericRepr('731.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('730.0'),
                GenericRepr('311.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.024440783970798935,
            0.2400290346120365,
            7606
        )
    },
    {
        'cartesian': [
            2020.3377600043916,
            -177.7299037662553,
            7145.636440902925
        ],
        'distance': 7427,
        'id': 54,
        'orientation': (
            -3.0395584730123235,
            -1.3221403997335517,
            -1.4857778259817267
        ),
        'pixel_centre': [
            926.0,
            295.0
        ],
        'pixel_corners': [
            [
                GenericRepr('877.0'),
                GenericRepr('308.0')
            ],
            [
                GenericRepr('878.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('852.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('852.0'),
                GenericRepr('309.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.024867381437367313,
            0.27554516722893785,
            7427
        )
    },
    {
        'cartesian': [
            2156.67287730126,
            -181.68124733650623,
            7362.175283051346
        ],
        'distance': 7673,
        'id': 54,
        'orientation': (
            3.1357278920429774,
            0.786524820056796,
            1.5856417660454294
        ),
        'pixel_centre': [
            938.0,
            259.0
        ],
        'pixel_corners': [
            [
                GenericRepr('889.0'),
                GenericRepr('345.0')
            ],
            [
                GenericRepr('889.0'),
                GenericRepr('309.0')
            ],
            [
                GenericRepr('915.0'),
                GenericRepr('309.0')
            ],
            [
                GenericRepr('915.0'),
                GenericRepr('345.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.024672650857571036,
            0.2849668671254678,
            7673
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203401.jpg-C270] 1'] = [
    {
        'cartesian': [
            -4.278651489335534,
            -79.85031016359937,
            1858.3067132121755
        ],
        'distance': 1860,
        'id': 54,
        'orientation': (
            -3.1070218011670905,
            -1.029871556831879,
            1.610886372213291
        ),
        'pixel_centre': [
            161.0,
            156.0
        ],
        'pixel_corners': [
            [
                GenericRepr('112.0'),
                GenericRepr('343.0')
            ],
            [
                GenericRepr('110.0'),
                GenericRepr('216.0')
            ],
            [
                GenericRepr('175.0'),
                GenericRepr('206.0')
            ],
            [
                GenericRepr('179.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.0429429757731973,
            -0.0023024422708009026,
            1860
        )
    },
    {
        'cartesian': [
            99.73491563380324,
            -80.83431302830807,
            1883.9280979514065
        ],
        'distance': 1888,
        'id': 54,
        'orientation': (
            3.0845148562765057,
            0.439149506167336,
            1.589798231134693
        ),
        'pixel_centre': [
            269.0,
            167.0
        ],
        'pixel_corners': [
            [
                GenericRepr('220.0'),
                GenericRepr('342.0')
            ],
            [
                GenericRepr('217.0'),
                GenericRepr('209.0')
            ],
            [
                GenericRepr('329.0'),
                GenericRepr('217.0')
            ],
            [
                GenericRepr('332.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.04288102156410237,
            0.052890499772393275,
            1888
        )
    },
    {
        'cartesian': [
            571.9480775930399,
            -100.13985450608754,
            2537.4457478715563
        ],
        'distance': 2603,
        'id': 52,
        'orientation': (
            -3.0804016768844367,
            -1.3207359741550995,
            -1.5154912516162953
        ),
        'pixel_centre': [
            768.0,
            288.0
        ],
        'pixel_corners': [
            [
                GenericRepr('719.0'),
                GenericRepr('237.0')
            ],
            [
                GenericRepr('721.0'),
                GenericRepr('339.0')
            ],
            [
                GenericRepr('673.0'),
                GenericRepr('338.0')
            ],
            [
                GenericRepr('671.0'),
                GenericRepr('244.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.03944435650004852,
            0.2216980630685447,
            2603
        )
    },
    {
        'cartesian': [
            654.6310366779835,
            -99.487531298726,
            2522.14085896417
        ],
        'distance': 2607,
        'id': 52,
        'orientation': (
            -3.137416617450789,
            0.571909844470826,
            0.012538399281592663
        ),
        'pixel_centre': [
            798.0,
            289.0
        ],
        'pixel_corners': [
            [
                GenericRepr('749.0'),
                GenericRepr('238.0')
            ],
            [
                GenericRepr('834.0'),
                GenericRepr('240.0')
            ],
            [
                GenericRepr('833.0'),
                GenericRepr('339.0')
            ],
            [
                GenericRepr('750.0'),
                GenericRepr('341.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.039425228571153895,
            0.25394998931733404,
            2607
        )
    },
    {
        'cartesian': [
            871.509902412247,
            -107.71556170719587,
            2839.9736712721833
        ],
        'distance': 2972,
        'id': 60,
        'orientation': (
            3.1012797750302674,
            0.7136259604963243,
            0.045122095115882666
        ),
        'pixel_centre': [
            968.0,
            288.0
        ],
        'pixel_corners': [
            [
                GenericRepr('919.0'),
                GenericRepr('244.0')
            ],
            [
                GenericRepr('1007.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('1007.0'),
                GenericRepr('338.0')
            ],
            [
                GenericRepr('920.0'),
                GenericRepr('338.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.03791019456696663,
            0.29774988008937725,
            2972
        )
    },
    {
        'cartesian': [
            978.996763122183,
            -110.84414638308169,
            3003.908029285937
        ],
        'distance': 3161,
        'id': 60,
        'orientation': (
            3.087021382651743,
            1.0477415847164546,
            1.6107958207438398
        ),
        'pixel_centre': [
            1084.0,
            193.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1035.0'),
                GenericRepr('337.0')
            ],
            [
                GenericRepr('1038.0'),
                GenericRepr('239.0')
            ],
            [
                GenericRepr('1078.0'),
                GenericRepr('243.0')
            ],
            [
                GenericRepr('1075.0'),
                GenericRepr('337.0')
            ]
        ],
        'size': 100,
        'spherical': (
            -0.03688324595332467,
            0.3150526654021497,
            3161
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203608.jpg-C270] 1'] = [
    {
        'cartesian': [
            289.3794123983702,
            44.90973876434696,
            1667.02945692283
        ],
        'distance': 1692,
        'id': 45,
        'orientation': (
            -2.9669046217884048,
            0.029697412152458445,
            3.136952675256492
        ),
        'pixel_centre': [
            691.0,
            327.0
        ],
        'pixel_corners': [
            [
                GenericRepr('642.0'),
                GenericRepr('527.0')
            ],
            [
                GenericRepr('494.0'),
                GenericRepr('525.0')
            ],
            [
                GenericRepr('497.0'),
                GenericRepr('377.0')
            ],
            [
                GenericRepr('643.0'),
                GenericRepr('381.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.02693346461603209,
            0.17187710326698852,
            1692
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203623.jpg-C270] 1'] = [
    {
        'cartesian': [
            615.5806147830598,
            30.409062504774912,
            1801.2551702849623
        ],
        'distance': 1903,
        'id': 52,
        'orientation': (
            -3.0834514944355544,
            0.9868414899141617,
            -1.567069004962243
        ),
        'pixel_centre': [
            1251.0,
            482.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1202.0'),
                GenericRepr('355.0')
            ],
            [
                GenericRepr('1211.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('1111.0'),
                GenericRepr('532.0')
            ],
            [
                GenericRepr('1104.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.01688054783577693,
            0.3293071572758295,
            1903
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203643.jpg-C270] 1'] = [
    {
        'cartesian': [
            615.5697588577118,
            30.408983709884126,
            1801.0434339067456
        ],
        'distance': 1903,
        'id': 52,
        'orientation': (
            -3.0807214701590357,
            0.9856773390957844,
            -1.5688818243654414
        ),
        'pixel_centre': [
            1252.0,
            482.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1203.0'),
                GenericRepr('355.0')
            ],
            [
                GenericRepr('1211.0'),
                GenericRepr('534.0')
            ],
            [
                GenericRepr('1111.0'),
                GenericRepr('532.0')
            ],
            [
                GenericRepr('1104.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.016882488252364714,
            0.32933773534056865,
            1903
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203703.jpg-C270] 1'] = [
    {
        'cartesian': [
            252.60114340531564,
            35.22710808642984,
            1564.5526920054965
        ],
        'distance': 1585,
        'id': 54,
        'orientation': (
            -3.0380749401807705,
            0.0965837203503277,
            1.5520533833009578
        ),
        'pixel_centre': [
            509.0,
            315.0
        ],
        'pixel_corners': [
            [
                GenericRepr('460.0'),
                GenericRepr('519.0')
            ],
            [
                GenericRepr('464.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('616.0'),
                GenericRepr('365.0')
            ],
            [
                GenericRepr('615.0'),
                GenericRepr('521.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.02251196598635397,
            0.16007130906483927,
            1585
        )
    },
    {
        'cartesian': [
            574.540259387511,
            37.73958423026057,
            1826.439594271735
        ],
        'distance': 1915,
        'id': 45,
        'orientation': (
            -3.0732684123695253,
            0.6663673324368136,
            3.1212367933221548
        ),
        'pixel_centre': [
            1136.0,
            325.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1087.0'),
                GenericRepr('531.0')
            ],
            [
                GenericRepr('928.0'),
                GenericRepr('528.0')
            ],
            [
                GenericRepr('926.0'),
                GenericRepr('375.0')
            ],
            [
                GenericRepr('1083.0'),
                GenericRepr('376.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.020659984962508707,
            0.30476817491846736,
            1915
        )
    }
]

snapshots['test_gets_markers_with_calibration[2019-06-08-203821.jpg-C270] 1'] = [
    {
        'cartesian': [
            10.815163830753228,
            37.76793500472289,
            1974.9929815172177
        ],
        'distance': 1975,
        'id': 54,
        'orientation': (
            2.9868779877922615,
            -1.249462509947138,
            1.5179269813414156
        ),
        'pixel_centre': [
            191.0,
            309.0
        ],
        'pixel_corners': [
            [
                GenericRepr('142.0'),
                GenericRepr('493.0')
            ],
            [
                GenericRepr('144.0'),
                GenericRepr('374.0')
            ],
            [
                GenericRepr('183.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('181.0'),
                GenericRepr('489.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.019120742482849687,
            0.0054759970433421595,
            1975
        )
    },
    {
        'cartesian': [
            108.5141149534567,
            34.39746973212966,
            1942.0425675367171
        ],
        'distance': 1945,
        'id': 54,
        'orientation': (
            3.1189092194694097,
            0.12172677650268669,
            1.5585483680942989
        ),
        'pixel_centre': [
            270.0,
            316.0
        ],
        'pixel_corners': [
            [
                GenericRepr('221.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('222.0'),
                GenericRepr('359.0')
            ],
            [
                GenericRepr('344.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('344.0'),
                GenericRepr('488.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.01771015423730071,
            0.055818237503316076,
            1945
        )
    },
    {
        'cartesian': [
            441.4274189102652,
            41.66715995536204,
            2209.653485557894
        ],
        'distance': 2253,
        'id': 45,
        'orientation': (
            -3.0376327923058386,
            0.15704574314351033,
            3.1330619367295203
        ),
        'pixel_centre': [
            736.0,
            326.0
        ],
        'pixel_corners': [
            [
                GenericRepr('687.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('579.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('579.0'),
                GenericRepr('376.0')
            ],
            [
                GenericRepr('688.0'),
                GenericRepr('379.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.01885464059740423,
            0.197176546986623,
            2253
        )
    },
    {
        'cartesian': [
            658.0691640734908,
            36.039073017784744,
            2280.2029485188013
        ],
        'distance': 2373,
        'id': 60,
        'orientation': (
            -3.078347935477998,
            0.5366682921909237,
            1.571842828376763
        ),
        'pixel_centre': [
            884.0,
            325.0
        ],
        'pixel_corners': [
            [
                GenericRepr('835.0'),
                GenericRepr('492.0')
            ],
            [
                GenericRepr('833.0'),
                GenericRepr('377.0')
            ],
            [
                GenericRepr('948.0'),
                GenericRepr('375.0')
            ],
            [
                GenericRepr('952.0'),
                GenericRepr('493.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.01580388823882312,
            0.28096659490260334,
            2373
        )
    },
    {
        'cartesian': [
            776.4373597699536,
            26.923240002553833,
            2357.163003644615
        ],
        'distance': 2481,
        'id': 52,
        'orientation': (
            -3.1013369352130016,
            0.9603254047449361,
            -1.557961959218717
        ),
        'pixel_centre': [
            1159.0,
            440.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1110.0'),
                GenericRepr('362.0')
            ],
            [
                GenericRepr('1116.0'),
                GenericRepr('491.0')
            ],
            [
                GenericRepr('1042.0'),
                GenericRepr('490.0')
            ],
            [
                GenericRepr('1037.0'),
                GenericRepr('372.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.011421386325802158,
            0.31820174339863255,
            2481
        )
    },
    {
        'cartesian': [
            847.6035102161021,
            24.61107745691945,
            2426.701306243966
        ],
        'distance': 2570,
        'id': 52,
        'orientation': (
            -3.1096390185608778,
            0.8971191200096716,
            -0.023410523590355805
        ),
        'pixel_centre': [
            1201.0,
            444.0
        ],
        'pixel_corners': [
            [
                GenericRepr('1152.0'),
                GenericRepr('363.0')
            ],
            [
                GenericRepr('1260.0'),
                GenericRepr('366.0')
            ],
            [
                GenericRepr('1263.0'),
                GenericRepr('494.0')
            ],
            [
                GenericRepr('1155.0'),
                GenericRepr('493.0')
            ]
        ],
        'size': 100,
        'spherical': (
            0.010141435061934545,
            0.33603518852250885,
            2570
        )
    }
]
