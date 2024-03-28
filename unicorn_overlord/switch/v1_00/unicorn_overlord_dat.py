# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

from . import kaitaistruct
from .kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class UnicornOverlordDat(ReadWriteKaitaiStruct):

    class EnumItemType(IntEnum):
        none = 0
        unknow = 1
        other = 2
        accessories = 3
        consumables = 4
        weapons = 5

    class EnumZenoiron(IntEnum):
        false = 0
        true = 16448

    class EnumUpgrade(IntEnum):
        false = 0
        true = 1

    class EnumItem(IntEnum):
        unknown = 0
        consume_start = 1
        gold = 2
        medal = 3
        colosseum_coin = 4
        collection_01 = 5
        retry = 6
        retry_veryhard = 7
        heal_one_s = 8
        heal_one_m = 9
        heal_one_l = 10
        heal_all_s = 11
        heal_all_m = 12
        heal_all_l = 13
        resurrection_s = 14
        resurrection_m = 15
        resurrection_l = 16
        heal_all_full = 17
        heal_stamina_s = 18
        heal_stamina_m = 19
        heal_stamina_l = 20
        sand_glass_s = 21
        sand_glass_m = 22
        sand_glass_l = 23
        campset_s = 24
        campset_m = 25
        campset_l = 26
        power_up = 27
        guard_up = 28
        exp_gold_up = 29
        speed_up = 30
        speed_up_2 = 31
        attract = 32
        attract_2 = 33
        assist_guard = 34
        regene = 35
        st_hide = 36
        st_nodamage = 37
        view_crystal = 38
        warp_1 = 39
        warp_2 = 40
        day_night = 41
        st_gimmick_1 = 42
        st_gimmick_2 = 43
        st_gimmick_3 = 44
        st_gimmick_4 = 45
        st_gimmick_5 = 46
        exp_01 = 47
        exp_02 = 48
        exp_03 = 49
        exp_04 = 50
        exp_05 = 51
        level_up = 52
        grow_hp = 53
        grow_patk = 54
        grow_pdef = 55
        grow_matk = 56
        grow_mdef = 57
        grow_hit = 58
        grow_eva = 59
        grow_cri = 60
        grow_grd = 61
        grow_spd = 62
        grow_all = 63
        ore_01 = 64
        ore_02 = 65
        edit_chara = 66
        goat_cookie = 67
        eat_ticket = 68
        dig_ticket = 69
        etc_01 = 70
        b_blue = 71
        b_key = 72
        cook_01 = 73
        cook_02 = 74
        cook_03 = 75
        cook_04 = 76
        cook_05 = 77
        cook_06 = 78
        cook_07 = 79
        cook_08 = 80
        cook_09 = 81
        cook_10 = 82
        cook_11 = 83
        cook_12 = 84
        cook_13 = 85
        cook_14 = 86
        cook_15 = 87
        cook_16 = 88
        cook_17 = 89
        gathering_25 = 90
        gathering_26 = 91
        gathering_27 = 92
        gathering_28 = 93
        gathering_29 = 94
        gathering_30 = 95
        gathering_31 = 96
        gathering_32 = 97
        gathering_33 = 98
        gathering_34 = 99
        gathering_35 = 100
        gathering_36 = 101
        gathering_37 = 102
        gathering_38 = 103
        gathering_39 = 104
        gathering_40 = 105
        gathering_41 = 106
        gathering_42 = 107
        gathering_43 = 108
        gathering_44 = 109
        gathering_45 = 110
        gathering_46 = 111
        gathering_47 = 112
        gathering_48 = 113
        gathering_49 = 114
        gathering_50 = 115
        gathering_51 = 116
        gathering_52 = 117
        gathering_53 = 118
        gathering_54 = 119
        gathering_55 = 120
        gathering_56 = 121
        gathering_57 = 122
        gathering_58 = 123
        gathering_59 = 124
        gathering_60 = 125
        gathering_61 = 126
        gathering_62 = 127
        gathering_63 = 128
        gathering_64 = 129
        gathering_65 = 130
        gathering_end = 131
        friend_start = 132
        friend_01 = 133
        friend_02 = 134
        friend_03 = 135
        friend_04 = 136
        friend_05 = 137
        friend_06 = 138
        friend_07 = 139
        friend_08 = 140
        friend_09 = 141
        friend_10 = 142
        friend_11 = 143
        friend_12 = 144
        friend_13 = 145
        friend_14 = 146
        friend_15 = 147
        friend_16 = 148
        friend_17 = 149
        friend_18 = 150
        friend_19 = 151
        friend_20 = 152
        friend_21 = 153
        friend_22 = 154
        friend_23 = 155
        friend_24 = 156
        friend_26 = 157
        friend_27 = 158
        friend_28 = 159
        friend_29 = 160
        friend_30 = 161
        friend_31 = 162
        friend_32 = 163
        friend_33 = 164
        friend_34 = 165
        friend_35 = 166
        friend_36 = 167
        friend_37 = 168
        friend_38 = 169
        friend_39 = 170
        friend_40 = 171
        graph_start = 172
        graph_c_1 = 173
        graph_c_2 = 174
        graph_c_3 = 175
        graph_c_4 = 176
        graph_c_5 = 177
        graph_c_6 = 178
        graph_d_1 = 179
        graph_d_2 = 180
        graph_d_3 = 181
        graph_d_4 = 182
        graph_d_5 = 183
        graph_d_6 = 184
        graph_e_1 = 185
        graph_e_2 = 186
        graph_e_3 = 187
        graph_e_4 = 188
        graph_e_5 = 189
        graph_e_6 = 190
        graph_b_1 = 191
        graph_b_2 = 192
        graph_b_3 = 193
        graph_b_4 = 194
        graph_b_5 = 195
        graph_b_6 = 196
        graph_a_1 = 197
        graph_a_2 = 198
        graph_a_3 = 199
        graph_a_4 = 200
        graph_a_5 = 201
        graph_a_6 = 202
        coa_start = 203
        coa_1 = 204
        coa_2 = 205
        coa_3 = 206
        coa_4 = 207
        coa_5 = 208
        coa_6 = 209
        coa_7 = 210
        coa_8 = 211
        coa_9 = 212
        coa_10 = 213
        coa_11 = 214
        coa_12 = 215
        coa_13 = 216
        coa_14 = 217
        coa_15 = 218
        coa_16 = 219
        coa_17 = 220
        coa_18 = 221
        coa_19 = 222
        coa_20 = 223
        coa_21 = 224
        coa_22 = 225
        coa_23 = 226
        coa_24 = 227
        coa_25 = 228
        coa_26 = 229
        coa_27 = 230
        coa_28 = 231
        coa_29 = 232
        coa_30 = 233
        coa_31 = 234
        coa_32 = 235
        coa_33 = 236
        coa_34 = 237
        coa_35 = 238
        coa_36 = 239
        coa_37 = 240
        coa_38 = 241
        coa_39 = 242
        coa_40 = 243
        coa_41 = 244
        coa_42 = 245
        coa_43 = 246
        coa_44 = 247
        coa_45 = 248
        coa_46 = 249
        coa_47 = 250
        coa_48 = 251
        coa_49 = 252
        coa_50 = 253
        coa_51 = 254
        coa_52 = 255
        coa_dlc_0 = 256
        coa_dlc_1 = 257
        coa_dlc_2 = 258
        coa_end = 259
        text_weapon_a = 260
        text_weapon_b = 261
        text_weapon_c = 262
        text_weapon_d = 263
        text_weapon_e = 264
        dig_game_time_s = 265
        dig_game_time_m = 266
        dig_game_time_l = 267
        consume_debug_1 = 268
        consume_debug_2 = 269
        consume_expand_01 = 270
        consume_expand_02 = 271
        consume_expand_03 = 272
        consume_expand_04 = 273
        consume_expand_05 = 274
        consume_expand_06 = 275
        consume_expand_07 = 276
        consume_expand_08 = 277
        consume_expand_09 = 278
        consume_expand_10 = 279
        consume_end = 280
        weapon_start = 281
        sword_01 = 282
        sword_01_1 = 283
        sword_01_2 = 284
        sword_01_3 = 285
        sword_02 = 286
        sword_02_1 = 287
        sword_02_2 = 288
        sword_02_3 = 289
        sword_03 = 290
        sword_03_1 = 291
        sword_03_2 = 292
        sword_03_3 = 293
        sword_max = 294
        sword_ex_start = 295
        sword_area_01 = 296
        sword_area_02 = 297
        sword_area_03 = 298
        sword_area_04 = 299
        sword_knight_start = 300
        sword_knight_01 = 301
        sword_knight_02 = 302
        sword_knight_03 = 303
        sword_knight_04 = 304
        sword_knight_05 = 305
        sword_status_start = 306
        sword_status_01 = 307
        sword_status_02 = 308
        sword_status_03 = 309
        sword_status_04 = 310
        sword_status_05 = 311
        sword_status_ex_01 = 312
        sword_status_ex_02 = 313
        sword_skill_start = 314
        sword_skill_01 = 315
        sword_skill_02 = 316
        sword_skill_03 = 317
        sword_skill_04 = 318
        sword_skill_05 = 319
        sword_skill_06 = 320
        sword_skill_07 = 321
        sword_skill_08 = 322
        sword_skill_09 = 323
        sword_skill_10 = 324
        sword_skill_11 = 325
        sword_skill_12 = 326
        sword_skill_13 = 327
        sword_skill_14 = 328
        sword_blood_01 = 329
        sword_magic_01 = 330
        sword_unique_start = 331
        sword_init_01 = 332
        sword_init_02 = 333
        sword_init_03 = 334
        sword_init_04 = 335
        sword_init_05 = 336
        sword_init_06 = 337
        sword_boss_01 = 338
        sword_boss_02 = 339
        sword_boss_03 = 340
        sword_unique_01 = 341
        sword_unique_02 = 342
        sword_legend_start = 343
        sword_legend_01 = 344
        sword_legend_02 = 345
        sword_legend_03 = 346
        sword_legend_04 = 347
        sword_legend_05 = 348
        lance_01 = 349
        lance_01_1 = 350
        lance_01_2 = 351
        lance_01_3 = 352
        lance_02 = 353
        lance_02_1 = 354
        lance_02_2 = 355
        lance_02_3 = 356
        lance_03 = 357
        lance_03_1 = 358
        lance_03_2 = 359
        lance_03_3 = 360
        lance_max = 361
        lance_ex_start = 362
        lance_area_01 = 363
        lance_area_02 = 364
        lance_area_03 = 365
        lance_area_04 = 366
        lance_tower_01 = 367
        lance_tower_02 = 368
        lance_knight_start = 369
        lance_knight_01 = 370
        lance_knight_02 = 371
        lance_knight_03 = 372
        lance_knight_04 = 373
        lance_knight_05 = 374
        lance_knight_06 = 375
        lance_status_start = 376
        lance_status_01 = 377
        lance_status_02 = 378
        lance_status_03 = 379
        lance_status_04 = 380
        lance_status_05 = 381
        lance_status_06 = 382
        lance_status_ex_01 = 383
        lance_status_ex_02 = 384
        lance_skill_start = 385
        lance_skill_01 = 386
        lance_skill_02 = 387
        lance_skill_03 = 388
        lance_skill_04 = 389
        lance_skill_05 = 390
        lance_skill_06 = 391
        lance_skill_07 = 392
        lance_skill_08 = 393
        lance_skill_09 = 394
        lance_skill_10 = 395
        lance_charge_01 = 396
        lance_blood_01 = 397
        lance_magic_01 = 398
        lance_unique_start = 399
        lance_init_01 = 400
        lance_init_02 = 401
        lance_init_03 = 402
        lance_boss_01 = 403
        lance_boss_02 = 404
        lance_boss_03 = 405
        lance_boss_04 = 406
        lance_boss_05 = 407
        lance_unique_01 = 408
        lance_legend_start = 409
        lance_legend_01 = 410
        lance_legend_02 = 411
        lance_legend_03 = 412
        lance_legend_04 = 413
        lance_legend_05 = 414
        axe_01 = 415
        axe_01_1 = 416
        axe_01_2 = 417
        axe_01_3 = 418
        axe_02 = 419
        axe_02_1 = 420
        axe_02_2 = 421
        axe_02_3 = 422
        axe_03 = 423
        axe_03_1 = 424
        axe_03_2 = 425
        axe_03_3 = 426
        axe_max = 427
        axe_ex_start = 428
        axe_area_01 = 429
        axe_area_02 = 430
        axe_area_03 = 431
        axe_area_04 = 432
        axe_knight_start = 433
        axe_knignt_01 = 434
        axe_knignt_02 = 435
        axe_knignt_03 = 436
        axe_knignt_04 = 437
        axe_knignt_05 = 438
        axe_knignt_06 = 439
        axe_status_start = 440
        axe_status_01 = 441
        axe_status_02 = 442
        axe_status_03 = 443
        axe_status_04 = 444
        axe_status_05 = 445
        axe_status_ex_01 = 446
        axe_status_ex_02 = 447
        axe_skill_start = 448
        axe_skill_01 = 449
        axe_skill_02 = 450
        axe_skill_03 = 451
        axe_skill_04 = 452
        axe_skill_05 = 453
        axe_skill_06 = 454
        axe_skill_07 = 455
        axe_skill_08 = 456
        axe_skill_09 = 457
        axe_skill_10 = 458
        axe_skill_11 = 459
        axe_skill_12 = 460
        axe_black_knight_01 = 461
        axe_gladiator_01 = 462
        axe_blood_01 = 463
        axe_magic_01 = 464
        axe_unique_start = 465
        axe_init_01 = 466
        axe_init_02 = 467
        axe_init_03 = 468
        axe_init_04 = 469
        axe_boss_01 = 470
        axe_boss_02 = 471
        axe_boss_03 = 472
        axe_boss_04 = 473
        axe_unique_01 = 474
        axe_regend_start = 475
        axe_regend_01 = 476
        axe_regend_02 = 477
        axe_regend_03 = 478
        axe_regend_04 = 479
        axe_regend_05 = 480
        bow_01 = 481
        bow_01_1 = 482
        bow_01_2 = 483
        bow_01_3 = 484
        bow_02 = 485
        bow_02_1 = 486
        bow_02_2 = 487
        bow_02_3 = 488
        bow_03 = 489
        bow_03_1 = 490
        bow_03_2 = 491
        bow_03_3 = 492
        bow_max = 493
        bow_ex_start = 494
        bow_area_01 = 495
        bow_area_02 = 496
        bow_area_03 = 497
        bow_area_04 = 498
        bow_tower_01 = 499
        bow_tower_02 = 500
        bow_knight_start = 501
        bow_knight_01 = 502
        bow_knight_02 = 503
        bow_knight_03 = 504
        bow_knight_04 = 505
        bow_knight_05 = 506
        bow_status_start = 507
        bow_status_01 = 508
        bow_status_02 = 509
        bow_status_03 = 510
        bow_status_04 = 511
        bow_status_05 = 512
        bow_status_06 = 513
        bow_skill_start = 514
        bow_skill_01 = 515
        bow_skill_02 = 516
        bow_skill_03 = 517
        bow_skill_04 = 518
        bow_skill_05 = 519
        bow_skill_06 = 520
        bow_skill_07 = 521
        bow_skill_08 = 522
        bow_skill_09 = 523
        bow_skill_10 = 524
        bow_skill_11 = 525
        bow_skill_12 = 526
        bow_skill_13 = 527
        bow_skill_14 = 528
        bow_skill_15 = 529
        bow_skill_16 = 530
        bow_charge_01 = 531
        bow_ranger_01 = 532
        bow_blood_01 = 533
        bow_magic_01 = 534
        bow_unique_start = 535
        bow_init_01 = 536
        bow_init_02 = 537
        bow_init_03 = 538
        bow_unique_01 = 539
        bow_unique_02 = 540
        bow_legend_start = 541
        bow_legend_01 = 542
        bow_legend_02 = 543
        bow_legend_03 = 544
        bow_legend_04 = 545
        bow_legend_05 = 546
        rod_01 = 547
        rod_01_1 = 548
        rod_01_2 = 549
        rod_01_3 = 550
        rod_02 = 551
        rod_02_1 = 552
        rod_02_2 = 553
        rod_02_3 = 554
        rod_03 = 555
        rod_03_1 = 556
        rod_03_2 = 557
        rod_03_3 = 558
        rod_max = 559
        rod_ex_start = 560
        rod_area_01 = 561
        rod_area_02 = 562
        rod_area_03 = 563
        rod_area_04 = 564
        rod_knight_start = 565
        rod_knight_1 = 566
        rod_knight_2 = 567
        rod_knight_3 = 568
        rod_knight_4 = 569
        rod_knight_5 = 570
        rod_knight_6 = 571
        rod_status_start = 572
        rod_status_01 = 573
        rod_status_02 = 574
        rod_status_03 = 575
        rod_status_04 = 576
        rod_status_05 = 577
        rod_status_06 = 578
        rod_status_07 = 579
        rod_status_08 = 580
        rod_skill_a_start = 581
        rod_skill_a_01 = 582
        rod_skill_a_02 = 583
        rod_skill_a_03 = 584
        rod_skill_a_04 = 585
        rod_skill_a_05 = 586
        rod_skill_a_06 = 587
        rod_skill_a_charge_01 = 588
        rod_skill_a_charge_02 = 589
        rod_skill_h_start = 590
        rod_barrier_01 = 591
        rod_barrier_02 = 592
        rod_heal_01 = 593
        rod_heal_02 = 594
        rod_heal_03 = 595
        rod_heal_04 = 596
        rod_heal_05 = 597
        rod_heal_06 = 598
        rod_resurrect_01 = 599
        rod_cure_01 = 600
        rod_skill_etc_start = 601
        rod_skill_etc_01 = 602
        rod_shaman_01 = 603
        rod_shaman_02 = 604
        rod_shaman_03 = 605
        rod_shaman_04 = 606
        rod_shaman_05 = 607
        rod_creric_01 = 608
        rod_unique_start = 609
        rod_init_01 = 610
        rod_init_02 = 611
        rod_init_03 = 612
        rod_boss_01 = 613
        rod_boss_02 = 614
        rod_boss_03 = 615
        rod_boss_04 = 616
        rod_boss_05 = 617
        rod_boss_06 = 618
        rod_boss_07 = 619
        rod_unique_01 = 620
        rod_unique_02 = 621
        rod_unique_03 = 622
        rod_legend_start = 623
        rod_legend_01 = 624
        rod_legend_02 = 625
        rod_legend_03 = 626
        rod_legend_04 = 627
        rod_legend_05 = 628
        rod_legend_end = 629
        weapon_expand_01 = 630
        weapon_expand_02 = 631
        weapon_expand_03 = 632
        weapon_expand_04 = 633
        weapon_expand_05 = 634
        weapon_expand_06 = 635
        weapon_expand_07 = 636
        weapon_expand_08 = 637
        weapon_expand_09 = 638
        weapon_expand_10 = 639
        weapon_end = 640
        shield_start = 641
        shield_01 = 642
        shield_01_1 = 643
        shield_01_2 = 644
        shield_01_3 = 645
        shield_02 = 646
        shield_02_1 = 647
        shield_02_2 = 648
        shield_02_3 = 649
        shield_03 = 650
        shield_03_1 = 651
        shield_03_2 = 652
        shield_03_3 = 653
        shield_max = 654
        shield_ex_start = 655
        shield_area_01 = 656
        shield_area_02 = 657
        shield_area_03 = 658
        shield_area_04 = 659
        shield_tower_01 = 660
        shield_tower_02 = 661
        shield_knight_start = 662
        shield_knight_01 = 663
        shield_knight_02 = 664
        shield_knight_03 = 665
        shield_knight_04 = 666
        shield_knight_05 = 667
        shield_knight_06 = 668
        shield_status_start = 669
        shield_status_01 = 670
        shield_status_02 = 671
        shield_status_03 = 672
        shield_status_04 = 673
        shield_status_05 = 674
        shield_resist_start = 675
        shield_resist_01 = 676
        shield_resist_02 = 677
        shield_resist_03 = 678
        shield_resist_04 = 679
        shield_resist_05 = 680
        shield_resist_06 = 681
        shield_resist_07 = 682
        shield_skill_start = 683
        shield_guard_01 = 684
        shield_guard_02 = 685
        shield_guard_03 = 686
        shield_guard_04 = 687
        shield_guard_05 = 688
        shield_guard_06 = 689
        shield_guard_07 = 690
        shield_guard_08 = 691
        shield_cover_01 = 692
        shield_cover_02 = 693
        shield_wall_01 = 694
        shield_wall_02 = 695
        shield_parry_01 = 696
        shield_skill_01 = 697
        shield_unique_start = 698
        shield_init_01 = 699
        shield_init_02 = 700
        shield_unique_01 = 701
        shield_unique_02 = 702
        shield_unique_03 = 703
        shield_legend_start = 704
        shield_legend_01 = 705
        shield_legend_02 = 706
        shield_legend_03 = 707
        shield_legend_04 = 708
        shield_legend_05 = 709
        shield_l_01 = 710
        shield_l_01_1 = 711
        shield_l_01_2 = 712
        shield_l_01_3 = 713
        shield_l_02 = 714
        shield_l_02_1 = 715
        shield_l_02_2 = 716
        shield_l_02_3 = 717
        shield_l_03 = 718
        shield_l_03_1 = 719
        shield_l_03_2 = 720
        shield_l_03_3 = 721
        shield_l_max = 722
        shield_l_ex_start = 723
        shield_l_area_01 = 724
        shield_l_area_02 = 725
        shield_l_area_03 = 726
        shield_l_area_04 = 727
        shield_l_knight_start = 728
        shield_l_knignt_01 = 729
        shield_l_knignt_02 = 730
        shield_l_knignt_03 = 731
        shield_l_knignt_04 = 732
        shield_l_knignt_05 = 733
        shield_l_knignt_06 = 734
        shield_l_status_start = 735
        shield_l_status_01 = 736
        shield_l_status_02 = 737
        shield_l_status_03 = 738
        shield_l_status_04 = 739
        shield_l_status_05 = 740
        shield_l_resist_start = 741
        shield_l_resist_01 = 742
        shield_l_resist_02 = 743
        shield_l_resist_03 = 744
        shield_l_resist_04 = 745
        shield_l_skill_start = 746
        shield_l_guard_01 = 747
        shield_l_guard_02 = 748
        shield_l_guard_03 = 749
        shield_l_guard_04 = 750
        shield_l_guard_05 = 751
        shield_l_guard_06 = 752
        shield_l_cover_01 = 753
        shield_l_cover_02 = 754
        shield_l_wall_01 = 755
        shield_l_wall_02 = 756
        shield_l_skill_01 = 757
        shield_l_skill_02 = 758
        shield_l_unique_start = 759
        shield_l_unique_01 = 760
        shield_l_unique_02 = 761
        shield_l_init_01 = 762
        shield_l_boss_01 = 763
        shield_l_boss_02 = 764
        shield_l_legend_start = 765
        shield_l_legend_01 = 766
        shield_l_legend_02 = 767
        shield_l_legend_03 = 768
        shield_l_legend_04 = 769
        shield_l_legend_05 = 770
        shield_l_legend_end = 771
        shield_expand_01 = 772
        shield_expand_02 = 773
        shield_expand_03 = 774
        shield_expand_04 = 775
        shield_expand_05 = 776
        shield_expand_06 = 777
        shield_expand_07 = 778
        shield_expand_08 = 779
        shield_expand_09 = 780
        shield_expand_10 = 781
        shield_end = 782
        accessory_start = 783
        acc_ap_pp_01 = 784
        acc_ap_pp_02 = 785
        acc_ap_pp_03 = 786
        acc_ap_pp_04 = 787
        acc_ap_pp_05 = 788
        acc_ap_pp_06 = 789
        acc_bangle_01 = 790
        acc_bangle_02 = 791
        acc_bangle_03 = 792
        acc_mdef_01 = 793
        acc_mdef_02 = 794
        acc_mdef_03 = 795
        acc_beret_01 = 796
        acc_beret_02 = 797
        acc_beret_03 = 798
        acc_hood_01 = 799
        acc_hood_02 = 800
        acc_hood_03 = 801
        acc_hp_01 = 802
        acc_hp_02 = 803
        acc_hp_03 = 804
        acc_spd_01 = 805
        acc_spd_02 = 806
        acc_spd_03 = 807
        acc_spd_04 = 808
        acc_spd_05 = 809
        acc_spd_06 = 810
        acc_hit_01 = 811
        acc_hit_02 = 812
        acc_eva_01 = 813
        acc_eva_02 = 814
        acc_cri_01 = 815
        acc_cri_02 = 816
        acc_cri_03 = 817
        acc_grd_01 = 818
        acc_grd_02 = 819
        acc_rege_01 = 820
        acc_rege_02 = 821
        acc_rege_03 = 822
        acc_rege_04 = 823
        acc_ribon_01 = 824
        acc_ribon_02 = 825
        acc_ribon_03 = 826
        acc_ribon_04 = 827
        acc_status_ex_01 = 828
        acc_status_ex_02 = 829
        acc_status_ex_03 = 830
        acc_status_ex_04 = 831
        acc_status_ex_05 = 832
        acc_status_ex_06 = 833
        acc_status_ex_07 = 834
        acc_status_ex_08 = 835
        acc_status_ex_09 = 836
        acc_tower_01 = 837
        acc_tower_02 = 838
        acc_tower_03 = 839
        acc_graveyard_01 = 840
        acc_graveyard_02 = 841
        acc_graveyard_03 = 842
        acc_graveyard_04 = 843
        acc_skill_up_01 = 844
        acc_skill_up_02 = 845
        acc_skill_up_03 = 846
        acc_btstart_start = 847
        acc_quickmove_01 = 848
        acc_quickmove_02 = 849
        acc_fast_strike_01 = 850
        acc_fast_strike_02 = 851
        acc_btstart_01 = 852
        acc_btstart_02 = 853
        acc_btstart_03 = 854
        acc_btstart_04 = 855
        acc_btstart_05 = 856
        acc_btstart_06 = 857
        acc_btstart_07 = 858
        acc_btstart_08 = 859
        acc_btend_start = 860
        acc_first_aid_01 = 861
        acc_first_aid_02 = 862
        acc_first_aid_03 = 863
        acc_btend_01 = 864
        acc_interrupt_start = 865
        acc_quick_barrier_01 = 866
        acc_quick_barrier_02 = 867
        acc_quick_barrier_03 = 868
        acc_evade_attach_01 = 869
        acc_evade_attach_02 = 870
        acc_saber_01 = 871
        acc_saber_02 = 872
        acc_saber_03 = 873
        acc_saber_04 = 874
        acc_interrupt_01 = 875
        acc_interrupt_02 = 876
        acc_interrupt_03 = 877
        acc_interrupt_04 = 878
        acc_interrupt_05 = 879
        acc_interrupt_06 = 880
        acc_interrupt_07 = 881
        acc_act_start_start = 882
        acc_eagle_eye_01 = 883
        acc_eagle_eye_02 = 884
        acc_eagle_eye_03 = 885
        acc_eagle_eye_04 = 886
        acc_act_start_01 = 887
        acc_act_end_start = 888
        acc_chase_01 = 889
        acc_chase_02 = 890
        acc_chase_03 = 891
        acc_chase_04 = 892
        acc_chase_05 = 893
        acc_counter_01 = 894
        acc_counter_02 = 895
        acc_counter_03 = 896
        acc_counter_04 = 897
        acc_counter_05 = 898
        acc_quick_heal_01 = 899
        acc_quick_heal_02 = 900
        acc_quick_cure_01 = 901
        acc_self_care_01 = 902
        acc_act_end_01 = 903
        acc_act_end_02 = 904
        acc_act_end_03 = 905
        acc_act_end_04 = 906
        acc_hit_before_start = 907
        acc_hit_before_01 = 908
        acc_hit_before_02 = 909
        acc_hit_before_03 = 910
        acc_hit_before_04 = 911
        acc_hit_before_05 = 912
        acc_hit_before_06 = 913
        acc_hit_before_07 = 914
        acc_hit_before_08 = 915
        acc_hit_after_start = 916
        acc_hit_after_01 = 917
        acc_hit_after_02 = 918
        acc_hit_after_03 = 919
        acc_hit_after_04 = 920
        acc_hit_after_05 = 921
        acc_skill_ex_01 = 922
        acc_skill_ex_02 = 923
        acc_skill_ex_03 = 924
        acc_cure_start = 925
        acc_cure_01 = 926
        acc_cure_02 = 927
        acc_cure_03 = 928
        acc_cure_04 = 929
        acc_cure_05 = 930
        acc_cure_06 = 931
        acc_cure_07 = 932
        acc_regist_01 = 933
        acc_regist_02 = 934
        acc_regist_03 = 935
        acc_regist_04 = 936
        acc_regist_ex_01 = 937
        acc_regist_ex_02 = 938
        acc_regist_ex_03 = 939
        acc_regist_ex_04 = 940
        acc_etc_start = 941
        acc_exp_gold_01 = 942
        acc_exp_gold_02 = 943
        acc_exp_gold_03 = 944
        acc_exp_gold_04 = 945
        acc_exp_gold_05 = 946
        acc_exp_gold_06 = 947
        acc_boss_01 = 948
        acc_boss_02 = 949
        acc_boss_03 = 950
        acc_charge_01 = 951
        acc_caster_sp_01 = 952
        acc_caster_sp_02 = 953
        acc_nekomimi_01 = 954
        acc_nekomimi_02 = 955
        acc_regend_01 = 956
        acc_regend_02 = 957
        acc_story_start = 958
        acc_story_01 = 959
        acc_story_02 = 960
        acc_story_03 = 961
        acc_story_04 = 962
        acc_story_05 = 963
        acc_story_06 = 964
        acc_debug_1 = 965
        acc_debug_2 = 966
        acc_debug_3 = 967
        acc_debug_4 = 968
        acc_debug_5 = 969
        acc_debug_6 = 970
        acc_debug_12 = 971
        acc_expand_01 = 972
        acc_expand_02 = 973
        acc_expand_03 = 974
        acc_expand_04 = 975
        acc_expand_05 = 976
        acc_expand_06 = 977
        acc_expand_07 = 978
        acc_expand_08 = 979
        acc_expand_09 = 980
        acc_expand_10 = 981

    class EnumDifficulty(IntEnum):
        casual = 0
        normal = 1
        tactical = 2
        expert = 3
    def __init__(self, _io=None, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._should_write_difficulty = False
        self.difficulty__to_write = True
        self._should_write_zenoiran = False
        self.zenoiran__to_write = True
        self._should_write_items = False
        self.items__to_write = True

    def _read(self):
        self.magic = self._io.read_bytes(8)
        if not (self.magic == b"\x00\x00\x00\x00\x55\x43\x53\x44"):
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x55\x43\x53\x44", self.magic, self._io, u"/seq/0")
        self.unknow = self._io.read_bytes(4)
        if not (self.unknow == b"\xD5\x50\x1C\x00"):
            raise kaitaistruct.ValidationNotEqualError(b"\xD5\x50\x1C\x00", self.unknow, self._io, u"/seq/1")
        self.file_size = self._io.read_u4le()
        self.slot = self._io.read_u4le()
        self.date_time = UnicornOverlordDat.DateTime(self._io, self, self._root)
        self.date_time._read()
        self.play_time = self._io.read_u4le()
        self.gold = self._io.read_u4le()
        self.renown = self._io.read_u4le()
        self.team_level = self._io.read_u4le()
        self.save_state = self._io.read_u4le()


    def _fetch_instances(self):
        pass
        self.date_time._fetch_instances()
        _ = self.difficulty
        _ = self.zenoiran
        _ = self.items
        for i in range(len(self._m_items)):
            pass
            self.items[i]._fetch_instances()



    def _write__seq(self, io=None):
        super(UnicornOverlordDat, self)._write__seq(io)
        self._should_write_difficulty = self.difficulty__to_write
        self._should_write_zenoiran = self.zenoiran__to_write
        self._should_write_items = self.items__to_write
        self._io.write_bytes(self.magic)
        self._io.write_bytes(self.unknow)
        self._io.write_u4le(self.file_size)
        self._io.write_u4le(self.slot)
        self.date_time._write__seq(self._io)
        self._io.write_u4le(self.play_time)
        self._io.write_u4le(self.gold)
        self._io.write_u4le(self.renown)
        self._io.write_u4le(self.team_level)
        self._io.write_u4le(self.save_state)


    def _check(self):
        pass
        if (len(self.magic) != 8):
            raise kaitaistruct.ConsistencyError(u"magic", len(self.magic), 8)
        if not (self.magic == b"\x00\x00\x00\x00\x55\x43\x53\x44"):
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x55\x43\x53\x44", self.magic, None, u"/seq/0")
        if (len(self.unknow) != 4):
            raise kaitaistruct.ConsistencyError(u"unknow", len(self.unknow), 4)
        if not (self.unknow == b"\xD5\x50\x1C\x00"):
            raise kaitaistruct.ValidationNotEqualError(b"\xD5\x50\x1C\x00", self.unknow, None, u"/seq/1")
        if self.date_time._root != self._root:
            raise kaitaistruct.ConsistencyError(u"date_time", self.date_time._root, self._root)
        if self.date_time._parent != self:
            raise kaitaistruct.ConsistencyError(u"date_time", self.date_time._parent, self)

    class DateTime(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.year = self._io.read_u2le()
            self.month = self._io.read_u1()
            self.day = self._io.read_u1()
            self.hour = self._io.read_u1()
            self.minute = self._io.read_u1()
            self.second = self._io.read_u1()
            self.unknow = self._io.read_u1()


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(UnicornOverlordDat.DateTime, self)._write__seq(io)
            self._io.write_u2le(self.year)
            self._io.write_u1(self.month)
            self._io.write_u1(self.day)
            self._io.write_u1(self.hour)
            self._io.write_u1(self.minute)
            self._io.write_u1(self.second)
            self._io.write_u1(self.unknow)


        def _check(self):
            pass


    class Item(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.id = KaitaiStream.resolve_enum(UnicornOverlordDat.EnumItem, self._io.read_u2le())
            self._unnamed1 = self._io.read_bytes(2)
            self.slot = self._io.read_u2le()
            self._unnamed3 = self._io.read_bytes(2)
            self.quantity = self._io.read_u2le()
            self._unnamed5 = self._io.read_bytes(1)
            self.not_sure = self._io.read_u1()
            self.equip = self._io.read_u4le()
            self.upgrade = KaitaiStream.resolve_enum(UnicornOverlordDat.EnumUpgrade, self._io.read_bits_int_be(4))
            self.type = KaitaiStream.resolve_enum(UnicornOverlordDat.EnumItemType, self._io.read_bits_int_be(4))
            self._unnamed10 = self._io.read_bytes(3)


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(UnicornOverlordDat.Item, self)._write__seq(io)
            self._io.write_u2le(int(self.id))
            self._io.write_bytes(self._unnamed1)
            self._io.write_u2le(self.slot)
            self._io.write_bytes(self._unnamed3)
            self._io.write_u2le(self.quantity)
            self._io.write_bytes(self._unnamed5)
            self._io.write_u1(self.not_sure)
            self._io.write_u4le(self.equip)
            self._io.write_bits_int_be(4, int(self.upgrade))
            self._io.write_bits_int_be(4, int(self.type))
            self._io.write_bytes(self._unnamed10)


        def _check(self):
            pass
            if (len(self._unnamed1) != 2):
                raise kaitaistruct.ConsistencyError(u"_unnamed1", len(self._unnamed1), 2)
            if (len(self._unnamed3) != 2):
                raise kaitaistruct.ConsistencyError(u"_unnamed3", len(self._unnamed3), 2)
            if (len(self._unnamed5) != 1):
                raise kaitaistruct.ConsistencyError(u"_unnamed5", len(self._unnamed5), 1)
            if (len(self._unnamed10) != 3):
                raise kaitaistruct.ConsistencyError(u"_unnamed10", len(self._unnamed10), 3)


    @property
    def difficulty(self):
        if self._should_write_difficulty:
            self._write_difficulty()
        if hasattr(self, '_m_difficulty'):
            return self._m_difficulty

        _pos = self._io.pos()
        self._io.seek(2117692)
        self._m_difficulty = KaitaiStream.resolve_enum(UnicornOverlordDat.EnumDifficulty, self._io.read_u4le())
        self._io.seek(_pos)
        return getattr(self, '_m_difficulty', None)

    @difficulty.setter
    def difficulty(self, v):
        self._m_difficulty = v

    def _write_difficulty(self):
        self._should_write_difficulty = False
        _pos = self._io.pos()
        self._io.seek(2117692)
        self._io.write_u4le(int(self.difficulty))
        self._io.seek(_pos)


    def _check_difficulty(self):
        pass

    @property
    def zenoiran(self):
        if self._should_write_zenoiran:
            self._write_zenoiran()
        if hasattr(self, '_m_zenoiran'):
            return self._m_zenoiran

        _pos = self._io.pos()
        self._io.seek(5088158)
        self._m_zenoiran = KaitaiStream.resolve_enum(UnicornOverlordDat.EnumZenoiron, self._io.read_u2le())
        self._io.seek(_pos)
        return getattr(self, '_m_zenoiran', None)

    @zenoiran.setter
    def zenoiran(self, v):
        self._m_zenoiran = v

    def _write_zenoiran(self):
        self._should_write_zenoiran = False
        _pos = self._io.pos()
        self._io.seek(5088158)
        self._io.write_u2le(int(self.zenoiran))
        self._io.seek(_pos)


    def _check_zenoiran(self):
        pass

    @property
    def items(self):
        if self._should_write_items:
            self._write_items()
        if hasattr(self, '_m_items'):
            return self._m_items

        _pos = self._io.pos()
        self._io.seek(160)
        self._m_items = []
        for i in range(4000):
            _t__m_items = UnicornOverlordDat.Item(self._io, self, self._root)
            _t__m_items._read()
            self._m_items.append(_t__m_items)

        self._io.seek(_pos)
        return getattr(self, '_m_items', None)

    @items.setter
    def items(self, v):
        self._m_items = v

    def _write_items(self):
        self._should_write_items = False
        _pos = self._io.pos()
        self._io.seek(160)
        for i in range(len(self._m_items)):
            pass
            self.items[i]._write__seq(self._io)

        self._io.seek(_pos)


    def _check_items(self):
        pass
        if (len(self.items) != 4000):
            raise kaitaistruct.ConsistencyError(u"items", len(self.items), 4000)
        for i in range(len(self._m_items)):
            pass
            if self.items[i]._root != self._root:
                raise kaitaistruct.ConsistencyError(u"items", self.items[i]._root, self._root)
            if self.items[i]._parent != self:
                raise kaitaistruct.ConsistencyError(u"items", self.items[i]._parent, self)



