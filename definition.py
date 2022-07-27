ptype_urqmd = {
        1:(0,"NN->NDelta"),
        2:(1,"NN->NN*"),
        3:(2,"NN->NDelta*"),
        4:(3,"NN->DeltaDelta"),
        5:(4,"NN->DeltaN*"),
        6:(5,"NN->DeltaDelta*"),
        7:(6,"NN->NN*,N*Delta*,Delta*Delta*"),
        8:(7,"NDelta->DeltaDelta"),
        10:(8,"MB->B'"),
        11:(9,"MM->M'"),
        13:(10,"BB (but not pp or pn) elastic scattering"),
        14:(11,"inelastic scattering (no string excitation)"),
        15:(12,"BB->2strings"),
        17:(13,"pn elastic"),
        19:(14,"pp elastic"),
        20:(15,"decay"),
        22:(16,"BBar elastic"),
        23:(17,"BBar annihilation->1string"),
        24:(18,"BBar diffractive->2strings"),
        26:(19,"MB elastic scattering"),
        27:(20,"MB,MM->1string"),
        28:(21,"MB,MM->2strings"),
        30:(22,"NDelta->NN"),
        31:(23,"DeltaDelta->DeltaN"),
        32:(24,"DeltaDelta->NN"),
        35:(25,"NDelta inelastic"),
        36:(26,"Danielewicz forward delay (MB->B')"),
        37:(27,"Danielewicz forward delay (MM->M')"),
        38:(28,"MM elastic scattering"),
        39:(29,"BBar inelastic scattering (no annihilation)"),
        40:(30,"Undocumented/unknown"),
        41:(31,"Undocumented/unknown"),
        42:(32,"Undocumented/unknown"),
        43:(33,"Undocumented/unknown"),
        55:(34,"Undocumented/unknown"),
        57:(35,"Undocumented/unknown"),
        58:(36,"Undocumented/unknown"),
        59:(37,"Undocumented/unknown"),
        60:(38,"Undocumented/unknown"),
        61:(39,"Undocumented/unknown"),
        62:(40,"Undocumented/unknown"),
        63:(41,"Undocumented/unknown"),
        64:(42,"Undocumented/unknown"),
        80:(43,"Periodic wall: Particle crosses the box wall"),
        81:(44,"Solid wall: Particle reflects off the box wall"),
        91:(45,"Fluidization"),
        96:(46,"Particlization"),
        -2:(47,"Undocumented/unknown"),
        -3:(48,"Undocumented/unknown"),
        -5:(49,"Undocumented/unknown"),
        -6:(50,"Undocumented/unknown")
        }

n_ptype_urqmd=len(ptype_urqmd)

ptype_smash = {
        0:(0,"None"),
        1:(1,"Elastic"),
        2:(2,"TwoToOne"),
        3:(3,"TwoToTwo"),
        4:(4,"TwoToThree"),
        15:(5,"TwoToFour"),
        13:(6,"TwoToFive"),
        5:(7,"Decay"),
        6:(8,"Wall"),
        7:(9,"Thermalization"),
        8:(10,"HyperSurfaceCrossing"),
        9:(11,"Bremsstrahlung"),
        10:(12,"MultiParticleThreeMesonsToOne"),
        11:(13,"MultiParticleThreeToTwo"),
        14:(14,"MultiParticleFourToTwo"),
        12:(15,"MultiParticleFiveToTwo"),
        41:(16,"StringSoftSingleDiffractiveAX"),
        42:(17,"StringSoftSingleDiffractiveXB"),
        43:(18,"StringSoftDoubleDiffractive"),
        44:(19,"StringSoftAnnihilation"),
        45:(20,"StringSoftNonDiffractive"),
        46:(21,"StringHard"),
        47:(22,"FailedString")
        }

n_ptype_smash=len(ptype_smash)

stable_urqmd = (1,17,27,40,49,55,101,102,103,106,107,109)
stable_smash = (111,211,221,223,331,333,311,321,2112,2212,3122,3112,3212,3222,3312,3322,3334)

n_star_tuple=(12112, 12212, 1214, 2124, 22112, 22212, 32112,\
  32212, 2116, 2216, 12116, 12216, 21214, 22124, 42112, 42212, 31214, 32124,\
  9902114, 9902214, 9952112, 9952212, 9962112, 9962212, 9912114, 9912214,\
  9902118, 9902218, 9922116, 9922216, 9922114, 9922214, 9972112, 9972212,\
  9932114, 9932214, 1218, 2128, 19922119, 19922219, 19932119, 19932219)


had_prop_dict = {
        "is_baryon":0,
        "is_meson":1,
        "is_antiparticle":2,
        "is_pion":3,
        "is_nucleon":4,
        "is_N_star":5,
        "is_stable":6
        }



def get_hadron_info_smash(pdg):
    if (pdg[0] == "-"):
        pdg=pdg[1:]
        is_antiparticle=1
    else:
        is_antiparticle=0
    len_pdg=len(pdg)
    int_pdg=int(pdg)
    q=[0,0,0]
    if(len_pdg==2): #it is a lepton
        B=0
        s=0
        kind=3
    else:
        q[0]=int(pdg[-2])
        q[1]=int(pdg[-3])
        if(len_pdg>3):
            q[2]=int(pdg[-4])
        if(q[2]>0): #it is a baryon
            B=1
        else:
            B=0 #2 quarks: it is a meson

        if(max(q)<4): #it is a hadron evolved by SMASH, it does not contain c or b quarks
            kind=1
        else:
            kind=2

    if B>0:
        is_baryon=1
        is_meson=0
    else:
        is_baryon=0
        if(kind != 3): # it is not a lepton
            is_meson=1
        else:
            is_meson=0

    if int_pdg in (111,211):
        is_pion=1
    else:
        is_pion=0

    if ((int_pdg in (2112,2212)) and (is_antiparticle==0)):
        is_nucleon=1
    else:
        is_nucleon=0

    if int_pdg in n_star_tuple:
        is_N_star=1
    else:
        is_N_star=0

    if int_pdg in stable_smash:
        is_stable=1
    else:
        is_stable=0
 
    return [is_baryon, is_meson, is_antiparticle, is_pion, is_nucleon, is_N_star, is_stable]


def get_hadron_info_urqmd(pid,charge):
    pid=int(pid)
    abs_pid=abs(pid)
    
    if ((pid < 0) or ((pid==101) and (charge==-1))):
        is_antiparticle=1
    else:
        is_antiparticle=0

    if (abs_pid == 101):
        is_pion=1
    else:
        is_pion=0

    if (pid == 1):
        is_nucleon=1
    else:
        is_nucleon=0

    if ((abs_pid > 1) and (abs_pid < 17)):
        is_N_star=1
    else:
        is_N_star=0

    if ((abs_pid < 55)):
        is_baryon=1
        is_meson=0
    else:
        is_baryon=0
        is_meson=1

    if abs_pid in stable_urqmd:
        is_stable=1
    else:
        is_stable=0

    return [is_baryon, is_meson, is_antiparticle, is_pion, is_nucleon, is_N_star, is_stable]
