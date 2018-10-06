import math

"""
1 - Calcula a entropia pra 298 K. A partir dela, calcula a estimativa da temperatura correspondente ao potencial químico fornecido pelo usuário. Digo estimativa, porque pra ser exato teríamos que usar a entropia correspondente à temperatura correta. Mas não sabemos a temperatura ainda. Estamos chutando 298 K, que provavelmente estará incorreta.
2 - Calcular a entropia a essa nova temperatura obtida. Essa temperatura já vai ser um palpite melhor que o palpite anterior.
3 - Com essa nova entropia e o mesmo potencial químico que o usuário forneceu no começo, calcular a nova estimativa de  temperatura correspondente ao potencial químico fornecido pelo usuário.
4 - Repetir passos 2 e 3 até a temperatura convergir.
"""


class Mu_to_temperature:
    def __init__(self, *args, **kwargs):
        self.coeff_100_700 = (31.322, -20.235, 57.866, -
                              36.506, -0.007, 246.794)
        self.coeff_700_2000 = (30.032, 8.773, -3.988, 0.788, -0.742, 236.166)
        self.coeff_2000_6000 = (20.911, 10.721, -2.020, 0.146, 9.246, 237.619)
        self.JmolK_to_eV = 0.00001036427230133
        self.atm_to_MPa = 101325.0e-6
        self.k_B = float(8.6173303e-5)
        self.mu_0k = -4.93552791875
        #self.t_over_1000 = T / 1000

    # This function returns the entropy of oxygen gas in eV
    def O2_entropy_in_eV_K(self, T):
        if T < 100:
            T = 100
        T_over_1000 = T / 1000

        # Use the appropriate coefficients for the desired temperature range. The coefficients and analytical expression for entropy were taken
        # from the Materials Project, based on experimental data

        if T >= 100 and T <= 700:
            entropy_JmolK = self.coeff_100_700[0] * math.log(T_over_1000) + self.coeff_100_700[1] * T_over_1000 + (self.coeff_100_700[2] * T_over_1000**2)/2.0 + (
                self.coeff_100_700[3] * T_over_1000**3)/3.0 - self.coeff_100_700[4]/(2.0 * T_over_1000**2) + self.coeff_100_700[5]
            entropy_eVK = entropy_JmolK * self.JmolK_to_eV
        elif T > 700 and T <= 2000:
            entropy_JmolK = self.coeff_100_700[0] * math.log(T_over_1000) + self.coeff_100_700[1] * T_over_1000 + (self.coeff_100_700[2] * T_over_1000**2)/2.0 + (
                self.coeff_100_700[3] * T_over_1000**3)/3.0 - self.coeff_100_700[4]/(2.0 * T_over_1000**2) + self.coeff_100_700[5]
            entropy_eVK = entropy_JmolK * self.JmolK_to_eV
        elif T > 2000 and T <= 6000:
            entropy_JmolK = self.coeff_100_700[0] * math.log(T_over_1000) + self.coeff_100_700[1] * T_over_1000 + (self.coeff_100_700[2] * T_over_1000**2)/2.0 + (
                self.coeff_100_700[3] * T_over_1000**3)/3.0 - self.coeff_100_700[4]/(2.0 * T_over_1000**2) + self.coeff_100_700[5]
            entropy_eVK = entropy_JmolK * self.JmolK_to_eV

        return entropy_eVK

    # This function calculates iteratively the temperature corresponding to a given oxygen chemical potential
    def temperature(self, mu):
        # We need an initial guess for temperature... Why not RT? =)
        T = 298.0
        # Just a dummy variable for the iterations
        T_old = 0

        # Do this until the temperature converges within 0.001 K
        while abs(T-T_old) > 1e-3:
            # The next three lines can be uncommented for debugging purposes. If you do this, also uncomment the line right above this loop
            T_old = T

            T = (mu - self.mu_0k)/(self.k_B - self.O2_entropy_in_eV_K(T) +
                                   self.k_B * math.log(0.21 * self.atm_to_MPa/0.1))

            if T < 0:
                T = 0

        return T

    def print_T_corresponding_to_mu_equals(self, mu):
        print(
            f'\n* Oxygen chemical potential: {mu:1.3f} eV * \nTemperature: {(self.temperature(mu)-273):3.2f} °C = {self.temperature(mu):3.2f} K')
        return {
            'potential': f'{mu:1.3f} eV',
            'celsius': f'{(self.temperature(mu)-273):3.2f} °C',
            'kelvin': f'{self.temperature(mu):3.2f} K',
        }
