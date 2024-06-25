# Import necessary dependencies
import pandas as pd
from io import StringIO

# Multiline string containing the data
data = """
Order Status;Date created;Sent to prod;Sales channel ID;Store name;Order type;Product Cost;Shipping Cost;Ship From;Tracking number;VAT / Tax cost;Total cost;Currency;Invoices
fulfilled;2023-01-01 0:37:08;2023-01-17 22:20:47;2744602167;GoldyTees;api;17.29 USD;6.39 USD;-;9400111108070462021014;0.00 USD;23.68;USD;2023.346409
fulfilled;2023-01-01 2:48:31;2023-01-07 20:58:15;2744697529;GoldyTees;api;4.77 USD;5.49 USD;-;92748901085901553042253693;0.00 USD;10.26;USD;2023.138892
fulfilled;2023-01-01 4:57:10;2023-01-07 21:04:49;2748765952;GoldyTees;api;11.29 USD;5.20 USD;-;9400111108070406761006;0.00 USD;16.49;USD;2023.139022
fulfilled;2023-01-01 14:43:22;2023-01-18 17:55:54;2748939466;GoldyTees;api;13.37 USD;4.90 USD;-;9274890278835152927996;0.00 USD;18.27;USD;
fulfilled;2023-01-01 15:48:41;2023-01-18 17:51:51;2745032125;GoldyTees;api;15.29 USD;8.50 USD;-;9400136109679350587285;0.00 USD;23.79;USD;
fulfilled;2023-01-01 22:27:38;2023-01-07 20:58:19;2749341876;GoldyTees;api;4.44 USD;5.89 USD;-;9400136109679310235522;0.00 USD;10.33;USD;2023.138896
canceled;2023-01-01 23:35:30;-;2745519937;GoldyTees;api;0.00 USD;0.00 USD;-;-;0.00 USD;0.0;USD;
fulfilled;2023-01-02 2:56:36;2023-01-07 20:56:33;2745677283;GoldyTees;api;10.07 USD;4.40 USD;-;9400136109679296000084;0.00 USD;14.47;USD;2023.138917
fulfilled;2023-01-02 4:03:44;2023-01-07 21:03:26;2745756453;GoldyTees;api;10.17 USD;4.40 USD;-;9400136109679295631173;0.00 USD;14.57;USD;2023.139023
payment-not-received;2023-01-02 15:07:29;-;2749881202;GoldyTees;api;26.64 USD;11.80 USD;-;-;0.00 USD;38.44;USD;
fulfilled;2023-01-02 15:07:29;2023-01-07 21:05:02;2749899054;GoldyTees;api;10.51 USD;4.69 USD;-;9400136109679292119438;0.00 USD;15.2;USD;2023.139034
fulfilled;2023-01-03 2:37:32;2023-01-18 17:56:22;2746825255;GoldyTees;api;15.62 USD;8.40 USD;-;9400136109679337399108;0.00 USD;24.02;USD;
fulfilled;2023-01-03 13:58:37;2023-01-18 17:56:20;2751035058;GoldyTees;api;16.08 USD;8.40 USD;-;9400136109679337688998;0.00 USD;24.48;USD;
fulfilled;2023-01-03 15:14:08;2023-01-07 20:58:52;2747195667;GoldyTees;api;2.79 USD;5.29 USD;-;9400111108070406543374;0.00 USD;8.08;USD;2023.138912
fulfilled;2023-01-04 2:20:55;2023-01-04 3:34:48;2751769142;GoldyTees;api;13.44 USD;9.69 USD;-;92612999964333543523362428;0.00 USD;23.13;USD;2023.61507
fulfilled;2023-01-04 20:01:55;2023-01-04 21:11:55;2748458581;GoldyTees;api;18.91 USD;8.50 USD;-;9400136109679276577636;0.00 USD;27.41;USD;2023.77877
canceled;2023-01-04 21:12:47;2023-01-24 16:48:10;2748566963;GoldyTees;api;14.26 USD;7.08 USD;-;-;0.00 USD;21.34;USD;
fulfilled;2023-01-04 22:23:22;2023-01-07 21:05:00;2752617592;GoldyTees;api;10.66 USD;4.69 USD;-;9400136109679304453260;0.00 USD;15.35;USD;2023.13903
fulfilled;2023-01-04 23:35:30;2023-01-07 20:58:53;2752733906;GoldyTees;api;5.17 USD;6.30 USD;-;420100359374810912401514325522;0.00 USD;11.47;USD;2023.138916
fulfilled;2023-01-04 23:35:30;2023-01-07 21:04:04;2752726912;GoldyTees;api;12.11 USD;4.90 USD;-;9274890278835152703330;0.00 USD;17.01;USD;2023.139014
fulfilled;2023-01-04 23:35:35;2023-01-18 17:56:22;2752694032;GoldyTees;api;15.62 USD;8.40 USD;-;9400136109679338087875;0.00 USD;24.02;USD;
fulfilled;2023-01-05 16:22:32;2023-01-18 17:56:02;2749297643;GoldyTees;api;13.37 USD;4.90 USD;-;9274890278835152928016;0.00 USD;18.27;USD;
fulfilled;2023-01-05 23:53:20;2023-01-07 21:10:09;2753808826;GoldyTees;api;13.56 USD;7.28 USD;-;9400111108070406389613;0.00 USD;20.84;USD;2023.139108
fulfilled;2023-01-06 1:09:00;2023-01-17 22:18:02;2749892133;GoldyTees;api;14.41 USD;10.00 USD;-;9405511108070462847143;0.00 USD;24.41;USD;2023.346342
fulfilled;2023-01-06 16:09:18;2023-01-24 16:59:08;2750379845;GoldyTees;api;16.08 USD;8.49 USD;-;9400136109679360978400;0.00 USD;24.57;USD;
fulfilled;2023-01-06 22:44:42;2023-01-24 16:45:45;2754838422;GoldyTees;api;19.48 USD;14.79 USD;-;9405536109679361115500;0.00 USD;34.27;USD;
fulfilled;2023-01-07 6:14:12;2023-01-18 17:56:23;2755271234;GoldyTees;api;14.41 USD;4.69 USD;-;9400136109679338168789;0.00 USD;19.1;USD;
fulfilled;2023-01-07 16:00:11;2023-01-18 17:55:57;2751387715;GoldyTees;api;13.37 USD;4.90 USD;-;9274890278835152928009;0.00 USD;18.27;USD;
fulfilled;2023-01-07 18:28:47;2023-01-18 17:56:08;2751508023;GoldyTees;api;15.62 USD;8.50 USD;-;420750819374810912401559183804;0.00 USD;24.12;USD;
fulfilled;2023-01-08 1:49:04;2023-01-18 17:51:50;2752012543;GoldyTees;api;14.75 USD;8.40 USD;-;9400136109679336333998;0.00 USD;23.15;USD;
fulfilled;2023-01-08 22:49:27;2023-01-13 19:18:46;2757139104;GoldyTees;api;12.11 USD;4.90 USD;-;9274890278835152808837;0.00 USD;17.01;USD;2023.262869
fulfilled;2023-01-09 5:05:20;2023-01-13 19:18:47;2753351505;GoldyTees;api;1.07 USD;4.39 USD;-;420336049374810912401537656856;0.00 USD;5.46;USD;2023.262868
fulfilled;2023-01-09 16:17:49;2023-01-13 19:18:51;2753666161;GoldyTees;api;2.79 USD;5.29 USD;-;9400111108070462316073;0.00 USD;8.08;USD;2023.26287
fulfilled;2023-01-09 20:12:55;2023-01-18 17:55:53;2758038302;GoldyTees;api;12.02 USD;15.20 USD;-;GM215362681008808970;0.00 USD;27.22;USD;
fulfilled;2023-01-12 23:50:21;2023-01-12 23:52:46;-;GoldyTees;manual;26.64 USD;16.69 USD;-;200800231000792047;0.00 USD;43.33;USD;
payment-not-received;2023-01-15 18:03:24;-;2764441252;GoldyTees;api;28.33 USD;6.19 USD;-;-;0.00 USD;34.52;USD;
in-production;2023-01-16 1:58:10;2023-01-18 17:56:03;2760582311;GoldyTees;api;13.37 USD;4.90 USD;-;-;0.00 USD;18.27;USD;
fulfilled;2023-01-16 1:58:10;2023-01-18 17:51:28;2760595835;GoldyTees;api;12.60 USD;4.40 USD;-;9400136109679334266809;0.00 USD;17.0;USD;
payment-not-received;2023-01-16 7:21:36;-;2765194716;GoldyTees;api;19.99 USD;8.59 USD;-;-;0.00 USD;28.58;USD;
canceled;2023-01-16 21:17:16;2023-01-18 17:56:00;2765825310;GoldyTees;api;13.37 USD;4.90 USD;-;-;0.00 USD;18.27;USD;
fulfilled;2023-01-16 22:43:51;2023-01-18 17:59:16;2761471785;GoldyTees;api;20.99 USD;8.50 USD;-;420301159361210912401553156396;0.00 USD;29.49;USD;
fulfilled;2023-01-17 4:16:50;2023-01-18 17:51:18;2761799783;GoldyTees;api;5.02 USD;4.89 USD;-;9400111108070462447517;0.00 USD;9.91;USD;
fulfilled;2023-01-19 4:00:20;2023-01-24 16:47:53;2763793617;GoldyTees;api;58.40 USD;21.31 USD;-;"9400136109679358294789;9400136109679358294789;9400136109679364102665;9400136109679364102665;9400136109679366988342;9400136109679366988342";0.00 USD;79.71;USD;
payment-not-received;2023-01-19 22:22:40;-;2764548403;GoldyTees;api;15.52 USD;4.89 USD;-;-;0.00 USD;20.41;USD;
fulfilled;2023-01-19 23:43:01;2023-01-20 0:51:47;2764669443;GoldyTees;api;1.60 USD;4.39 USD;-;420950509374810912401577158273;0.00 USD;5.99;USD;
fulfilled;2023-01-19 23:43:02;2023-01-20 0:52:02;2764601155;GoldyTees;api;7.52 USD;4.49 USD;-;Tracking not available;0.00 USD;12.01;USD;
payment-not-received;2023-01-20 16:24:07;-;2765295029;GoldyTees;api;26.72 USD;8.50 USD;-;-;0.00 USD;35.22;USD;
fulfilled;2023-01-20 19:24:34;2023-01-24 16:53:40;2765493149;GoldyTees;api;10.51 USD;4.75 USD;-;9400136109679356336207;0.00 USD;15.26;USD;
on-hold;2023-01-20 19:24:34;-;2765433641;GoldyTees;api;13.84 USD;4.69 USD;-;-;0.00 USD;18.53;USD;
fulfilled;2023-01-21 2:38:06;2023-01-24 16:54:00;2765938103;GoldyTees;api;10.51 USD;4.75 USD;-;9400136109679360669940;0.00 USD;15.26;USD;
fulfilled;2023-01-21 15:14:04;2023-01-21 16:21:19;2766324841;GoldyTees;api;4.91 USD;4.89 USD;-;9400111108070469680870;0.00 USD;9.8;USD;
fulfilled;2023-01-22 1:24:46;2023-01-22 2:34:55;2766953633;GoldyTees;api;10.26 USD;4.80 USD;-;9400111206213604842752;0.00 USD;15.06;USD;
fulfilled;2023-01-22 18:28:23;2023-01-22 19:35:34;2771839836;GoldyTees;api;10.34 USD;8.59 USD;-;9400111206213663134935;0.00 USD;18.93;USD;
fulfilled;2023-01-23 3:29:39;2023-01-23 4:32:06;2772491228;GoldyTees;api;4.91 USD;4.89 USD;-;9400111108070464116930;0.00 USD;9.8;USD;
fulfilled;2023-01-24 16:38:00;2023-01-24 17:42:55;2769875643;GoldyTees;api;15.62 USD;12.69 USD;-;4OX2Z9KWEGL4QURDP0KTAK;0.00 USD;28.31;USD;
fulfilled;2023-01-24 16:38:01;2023-01-24 17:40:54;2769760953;GoldyTees;api;9.92 USD;4.75 USD;-;9400136109679363914634;0.00 USD;14.67;USD;
fulfilled;2023-01-24 21:14:25;2023-01-24 22:20:33;2770152391;GoldyTees;api;10.53 USD;4.75 USD;-;9400136109679369197611;0.00 USD;15.28;USD;
payment-not-received;2023-01-25 0:20:35;-;2774362706;GoldyTees;api;5.17 USD;6.29 USD;-;-;0.00 USD;11.46;USD;
payment-not-received;2023-01-25 3:20:05;-;2770513933;GoldyTees;api;22.60 USD;5.50 USD;-;-;0.00 USD;28.1;USD;
payment-not-received;2023-01-25 3:20:05;-;2770555779;GoldyTees;api;22.60 USD;5.50 USD;-;-;0.00 USD;28.1;USD;
payment-not-received;2023-01-25 6:14:35;-;2774605952;GoldyTees;api;15.62 USD;8.49 USD;-;-;0.00 USD;24.11;USD;
payment-not-received;2023-01-25 16:16:39;-;2771014059;GoldyTees;api;21.02 USD;7.15 USD;-;-;0.00 USD;28.17;USD;
fulfilled;2023-01-25 17:49:06;2023-01-25 18:50:54;2771089479;GoldyTees;api;13.37 USD;4.50 USD;-;92748901790444543432183283;0.00 USD;17.87;USD;
on-hold;2023-01-26 5:45:15;-;2771773949;GoldyTees;api;12.64 USD;5.69 USD;-;-;0.00 USD;18.33;USD;
fulfilled;2023-01-26 13:02:08;2023-01-26 14:11:08;2775783702;GoldyTees;api;8.06 USD;5.99 USD;-;GM215362681008826691;0.00 USD;14.05;USD;
payment-not-received;2023-01-26 15:04:22;-;2771745357;GoldyTees;api;8.32 USD;10.00 USD;-;-;0.00 USD;18.32;USD;
in-production;2023-01-26 16:03:24;2023-01-26 17:11:41;2772145897;GoldyTees;api;1.07 USD;4.29 USD;-;-;0.00 USD;5.36;USD;
payment-not-received;2023-01-26 19:06:01;-;2772374623;GoldyTees;api;10.66 USD;4.75 USD;-;-;0.00 USD;15.41;USD;
payment-not-received;2023-01-26 23:36:18;-;2772656353;GoldyTees;api;23.91 USD;7.08 USD;-;-;0.00 USD;30.99;USD;
payment-not-received;2023-01-27 4:09:25;-;2772883683;GoldyTees;api;13.37 USD;4.50 USD;-;-;0.00 USD;17.87;USD;
payment-not-received;2023-01-27 18:58:13;-;2776974634;GoldyTees;api;12.87 USD;5.00 USD;-;-;0.00 USD;17.87;USD;
payment-not-received;2023-01-27 18:58:13;-;2777000330;GoldyTees;api;15.62 USD;8.49 USD;-;-;0.00 USD;24.11;USD;
payment-not-received;2023-01-27 23:27:19;-;2773775727;GoldyTees;api;8.06 USD;5.99 USD;-;-;0.00 USD;14.05;USD;
payment-not-received;2023-01-28 0:54:39;-;2777378378;GoldyTees;api;6.78 USD;5.29 USD;-;-;0.00 USD;12.07;USD;
payment-not-received;2023-01-28 23:19:34;-;2774901369;GoldyTees;api;10.66 USD;9.39 USD;-;-;0.00 USD;20.05;USD;
payment-not-received;2023-01-29 0:48:54;-;2778337660;GoldyTees;api;10.26 USD;5.19 USD;-;-;0.00 USD;15.45;USD;
payment-not-received;2023-01-29 14:04:02;-;2775466373;GoldyTees;api;12.47 USD;5.19 USD;-;-;0.00 USD;17.66;USD;
"""

# Use StringIO to convert the string data into a file-like object
data_io = StringIO(data)

# Read the CSV data using pandas, specifying the delimiter
df = pd.read_csv(data_io, delimiter=';')

# Filter rows where 'Tracking number' starts with 'GM'
gm_tracking_numbers = df[df['Tracking number'].str.startswith('GM', na=False)]

# Count the number of such rows
number_of_gm_trackings = gm_tracking_numbers.shape[0]

# Print the count
print(number_of_gm_trackings)