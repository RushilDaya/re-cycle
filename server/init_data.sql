INSERT INTO user (name,surname,age,budget,discount_diff,city_id,company_id) VALUES ('John','Doe',23,300,25,1,1);
INSERT INTO user (name,surname,age,budget,discount_diff,city_id,company_id) VALUES ('Mary','Major',42,400,15,1,2);
INSERT INTO user (name,surname,age,budget,discount_diff,city_id,company_id) VALUES ('Grace','Goe',18,250,10,2,1);
INSERT INTO user (name,surname,age,budget,discount_diff,city_id,company_id) VALUES ('Richard','Miles',30,600,0,2,2);

INSERT INTO company (name) VALUES ('Tobania');
INSERT INTO company (name) VALUES ('AFT');

INSERT INTO city (name) VALUES ('Leuven');
INSERT INTO city (name) VALUES ('Gent');

INSERT INTO route (user_id,route_date,total_km) VALUES (1,'2019-01-01',3);
INSERT INTO route (user_id,route_date,total_km) VALUES (2,'2019-01-01',4);
INSERT INTO route (user_id,route_date,total_km) VALUES (3,'2019-01-01',2);
INSERT INTO route (user_id,route_date,total_km) VALUES (4,'2019-01-01',1);
INSERT INTO route (user_id,route_date,total_km) VALUES (1,'2019-01-02',3);
INSERT INTO route (user_id,route_date,total_km) VALUES (2,'2019-01-02',4);
INSERT INTO route (user_id,route_date,total_km) VALUES (3,'2019-01-02',2);
INSERT INTO route (user_id,route_date,total_km) VALUES (4,'2019-01-02',1);
INSERT INTO route (user_id,route_date,total_km) VALUES (1,'2019-01-03',2);
INSERT INTO route (user_id,route_date,total_km) VALUES (2,'2019-01-03',1);
INSERT INTO route (user_id,route_date,total_km) VALUES (3,'2019-01-03',2);
INSERT INTO route (user_id,route_date,total_km) VALUES (4,'2019-01-03',1);
INSERT INTO route (user_id,route_date,total_km) VALUES (1,'2019-01-04',2);
INSERT INTO route (user_id,route_date,total_km) VALUES (2,'2019-01-04',3);
INSERT INTO route (user_id,route_date,total_km) VALUES (3,'2019-01-04',2);
INSERT INTO route (user_id,route_date,total_km) VALUES (4,'2019-01-04',1);
INSERT INTO route (user_id,route_date,total_km) VALUES (1,'2019-01-05',3);
INSERT INTO route (user_id,route_date,total_km) VALUES (2,'2019-01-05',4);
INSERT INTO route (user_id,route_date,total_km) VALUES (3,'2019-01-05',3);
INSERT INTO route (user_id,route_date,total_km) VALUES (4,'2019-01-05',1);
INSERT INTO route (user_id,route_date,total_km) VALUES (1,'2019-01-06',2);
INSERT INTO route (user_id,route_date,total_km) VALUES (2,'2019-01-06',4);
INSERT INTO route (user_id,route_date,total_km) VALUES (3,'2019-01-06',2);
INSERT INTO route (user_id,route_date,total_km) VALUES (4,'2019-01-06',1);
INSERT INTO route (user_id,route_date,total_km) VALUES (1,'2019-01-07',3);
INSERT INTO route (user_id,route_date,total_km) VALUES (2,'2019-01-07',4);
INSERT INTO route (user_id,route_date,total_km) VALUES (3,'2019-01-07',3);
INSERT INTO route (user_id,route_date,total_km) VALUES (4,'2019-01-07',2);

INSERT INTO discount (name,url,img,discount_rate) VALUES ('NMBS','https://www.belgiantrain.be','https://seeklogo.com/images/N/NMBS_-_SNCB-logo-5E5F5EA38E-seeklogo.com.png',10);
INSERT INTO discount (name,url,img,discount_rate) VALUES ('De Lijn','https://www.delijn.be','https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/De_Lijn.svg/266px-De_Lijn.svg.png',12);
INSERT INTO discount (name,url,img,discount_rate) VALUES ('UBER','https://www.uber.com','https://image.advance.net/home/advance-media/width460/img/newyorkupstatecom_national_desk_blog/photo/2018/03/15/uberjpg-5f9a611fad597f9c.jpg',5);
INSERT INTO discount (name,url,img,discount_rate) VALUES ('VELO','https://www.velo.be','https://www.velo.be/sites/all/themes/velo/images/logo_velo_wit.png',15);
INSERT INTO discount (name,url,img,discount_rate) VALUES ('BLABLACAR','https://www.blablacar.com','https://www.vostoknewventures.com/wp-content/uploads/2015/10/bla_bla_car_logo.png',7.5);