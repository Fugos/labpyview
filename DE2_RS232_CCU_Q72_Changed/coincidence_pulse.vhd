-- The counter
LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY coincidence_pulse IS
	PORT
	(
		a, b, c, d, e, f, g, h	:IN 	STD_LOGIC;
		y			:OUT 	STD_LOGIC
	);
END coincidence_pulse;

ARCHITECTURE circuit OF coincidence_pulse IS
BEGIN
-- The output y will give a pulse for each coincidence of four simultaneos photons
-- The variables e through h represent the switches SW(5) to SW(2) on the DE2 Board
-- If on of these switches is on then the signal from the corresponing photon detector is ignored
	y <= (a or NOT e) and (b or NOT f) and (c or NOT g) and (d or NOT h);
END circuit;