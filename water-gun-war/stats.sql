-- close file menu to view full table
.mode columns
create table water_gun_stats 
( 
  id integer primary key,
  gun_name text,
  range integer,
  max_ammo integer,
  shoot_liters integer,
  notes text
);


insert into water_gun_stats values(1, 'Four Sprayer', 3, 1, 0.25, null);
insert into water_gun_stats values(2, 'Pumper', 6, 1.5, 0.5, 'Unavailable in physcial');
insert into water_gun_stats values(3, 'One Spray', 6, 0.5, 0.5, null);
insert into water_gun_stats values(4, 'Hose', 12, 100, 100, null);
insert into water_gun_stats values(5, 'Wet nerf', 12, 4, 1, 'Measurements in nerf darts(range is normal)');
insert into water_gun_stats values(6, 'Balloon Bomb', 100, 1, 0.25, null);
insert into water_gun_stats values(7, 'Wet ball', 100, 1, 1, 'Measurements in balls(range is normal)');
insert into water_gun_stats values(8, 'Triple balls', 100, 3, 3, 'Measurements in balls(range is normal)');
insert into water_gun_stats values(9, 'Water can', 3, 100, 100, null);
insert into water_gun_stats values(10, 'Soaked fists', 3, 2, 1, 'Measurements in fists(range is normal)');
insert into water_gun_stats values(11, 'Wave', 6, null, null, 'Pushes back anyone in range. Anyone can use it, but only thrice.');
insert into water_gun_stats values(12, 'Bottle', 3, 0.5, 0.25, null);
insert into water_gun_stats values(13, 'Cup', 3, 0.25, 0.25, null);
insert into water_gun_stats values(14, 'Shield', null, null, null, 'Blocks anything in front.');
insert into water_gun_stats values(15, 'Foam Pump', 6, 0.75, 0.5, null);
insert into water_gun_stats values(16, 'Trash minigun', 12, 0.75, 0.25, null);
insert into water_gun_stats values(17, 'Healing waters', 12, 1, 1, 'Gun that heals 1 life and Measurements in nerf darts(range is normal).');
insert into water_gun_stats values(18, 'Portable Reload Station', null, 2, null, 'Activate for a in-game relaod station.');
insert into water_gun_stats values(19, 'Wet foam ball', 100, 2, 1, 'Measurements in balls(range is normal)');
insert into water_gun_stats values(20, 'Water', 100, 100, 100, 'Any weapon');


/* id, Gun name, Range, Max ammo, Shoot liters */
.width 25 -- if doing everything xept id
-- .width 25, 75 --if doing gun_name and notes
select gun_name, range, max_ammo, shoot_liters from water_gun_stats where range <= 10 and max_ammo <= 10 and shoot_liters <= 10;