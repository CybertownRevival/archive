#VRML V2.0 utf8

##############################							 
# OBJECT CHECKER VERSION 2.0 #
#----------------------------####
# CREATED BY: LEE CLAGETT (008) #
#-------------------------------##########################
# THIS IS NOT TO BE USED BY ANYONE WITHOUT THE EXPRESS	 #
# WRITTING CONSENT OF LEE CLAGETT                        #
# COPYRIGHT 2001					 #				 #
##########################################################


Transform {
 translation 0 -1.75 0
 children [
  Shape {
   appearance Appearance {
    material Material {
     transparency 1
    }
   }
   geometry Box { size 100 .01 100 }
  }
 ]
}

PointLight {
intensity 1
on TRUE
radius 100
}

DEF MAIN_VIEW Viewpoint {
 position 0 0 8.8
 description "Front View"
}
DEF FLOOR_VIEW Viewpoint {
 position 0 -1.75 3.1
 description "Floor"
}

DEF BACK Background {
	skyColor 0 0 0
}

DEF PROX_SENSOR ProximitySensor { 
 size 10 10 10
 center 0 0 6.8
}

##############################################
# THIS IS FOR THE OBJECT SOMEONE IS CHECKING #
##############################################----------------------#
# The variable object is the path to the vrml file on their         #
# computer. This places that path in the inline field, making their #
# object display on screen. It is centered at 0, 0, 0 which forces  #
# the User to make sure that the bottom is at 0 -1.75 0             #
#-------------------------------------------------------------------#
Inline {
 url [""]
}

WorldInfo {
	title "Mall Object Viewer V2.0"
	info ["This Object Viewer was" 
		  "created by:"
		"Lee Clagett (008)"]
	}


#####################################
# MAIN BOX PLATFORM, AND HIDDEN ONE #
#####################################
 PROTO PLATFORM [
	 exposedField SFVec3f translation 0 -1.75 0
	 exposedField SFColor diffuseColor 0 0 1
	 exposedField SFFloat transparency .5
	 field SFVec3f size 3 .01 3
	 field SFVec3f size2 10 .01 10
	 exposedField SFInt32 whichChoice 0
]
{
	Switch {
		whichChoice	IS whichChoice
		choice [
Transform { 
 translation IS translation
 children [
  Shape {
   appearance Appearance {
    material Material {  
     diffuseColor IS diffuseColor 
     transparency IS transparency
    }
   }
   geometry Box { size IS size }
  }
 ]
}
Transform { children [ ] }
Transform {
	translation	IS translation
	children [
		Shape {
			appearance Appearance {
				material Material {
					diffuseColor IS	diffuseColor
					transparency IS	transparency
				}
			}
			geometry Box { size	IS size2 }
		}
	]
}
]
}
}

DEF FLOOR PLATFORM { whichChoice 0 }
DEF	BWALL PLATFORM { whichChoice 1 translation 0 -.25 -1.5 diffuseColor 0 0 1 transparency	.5 size	3 3 .01 size2 10 10 .01}
DEF	RWALL PLATFORM { whichChoice 1 translation 1.5 -.25 0 diffuseColor 0 0 1 transparency	.5 size	.01 3 3 size2 .01 10 10}
DEF	LWALL PLATFORM { whichChoice 1 translation -1.5 -.25 0 diffuseColor 0 0 1 transparency	.5 size	.01 3 3 size2 .01 10 10}
DEF	FWALL PLATFORM { whichChoice 1 translation 0 -.25 1.5 diffuseColor 0 0 1 transparency	.5 size	3 3 .01 size2 10 10 .01}
DEF	ROOF PLATFORM { whichChoice 1 translation 0 1.25 0 diffuseColor 0 0 1 transparency	.5 size	3 .01 3 size2 10 .01 10}

###########################
# COMPARE TO A DEFAULT AV #
###########################
Transform {
 children [ 
  DEF MOVE_SENSOR PlaneSensor {
   maxPosition 6 -.1
   minPosition -6 -.1
  }
   DEF AVATAR Transform {
    translation 6 -.1 0 
    children [ 
     Inline {
      url ["http://www.blaxxun.com/vrml/avatars/default.wrl"]
     }
    ]
   }
 ]
}


##############
# GRID LINES #
##############

Transform { 
 translation 0 -1.75 0
 children [
Shape {
 appearance Appearance {
  material Material {
   emissiveColor 1 .9764705 0
  }
 }
 geometry IndexedLineSet {
  coord Coordinate {
   point [0 4.5 0, 0 -4.5 0]
  }
  coordIndex [0, 1, -1]
 }
}
Shape {
 appearance Appearance {
  material Material {
   emissiveColor 1 .9764705 0
  }
 }
 geometry IndexedLineSet {
  coord Coordinate {
   point [6.5 0 0, -6.5 0 0]
  }
  coordIndex [0, 1, -1]
 }
}
Shape {
 appearance Appearance {
  material Material {
   emissiveColor 1 .9764705 0
  }
 }
 geometry IndexedLineSet {
  coord Coordinate {
   point [0 0 4.5, 0 0 -4.5]
  }
  coordIndex [0, 1, -1]
 }
} 
Shape {
 appearance Appearance {
  material Material {
   emissiveColor 1 0 0
  }
 }
 geometry IndexedLineSet {
 coord Coordinate {
   point [-5 0 1, 5 0 1]
          
  }
  coordIndex [0, 1, -1]
 }
}
]
}
###############
# END OF GRID # 
###############
 
####################################
# NAVIGATION BAR - PROTO FOR BOXES #
####################################
PROTO Box_Navigation [
	exposedField SFVec3f translation 0 0 0
	exposedField SFColor diffuseColor .5 0 0
	exposedField MFString string "Default"
	field SFInt32 box 0
	exposedField SFFloat transparency 0
	exposedField SFInt32 whichChoice 0
]
{
	Switch {
		whichChoice	IS whichChoice
		choice [
	Transform {
		 translation IS	translation
		 children [
			 Shape {
				 appearance	Appearance {
					 material DEF MATERIAL Material {
						 diffuseColor IS diffuseColor
						 transparency IS transparency
					 }
				 }
				 geometry Box { size .06 .015 .00001 }
			 }
			 Transform {
				 translation -.023 -.004 .005
				 children [
			 Shape {
				 appearance	Appearance {
					 material Material {
						 diffuseColor 1 1 1
						 transparency IS transparency
					 }
				 }
				 geometry Text {
					 string	IS string
					 fontStyle FontStyle {
						 size .01
						 
					 }
				 }
			 }
		 ]
	 }
		 ]
	 }
	 Transform { children []}
 ]
}
 }

 PROTO Lines [
	 exposedField MFVec3f point [0 0 0]
	 field MFInt32 coordIndex [0, -1]
	 exposedField SFFloat transparency 0
	 exposedField SFInt32 whichChoice 0
	 exposedField SFColor diffuseColor 1 1 1
 ]
 {
Switch	{
whichChoice IS whichChoice
choice	[
Group { 
	children [
Shape {
 appearance Appearance {
  material Material {
   diffuseColor IS diffuseColor
   transparency	IS transparency
  }
 }
 geometry IndexedLineSet {
  coord Coordinate {
   point IS	point
          
  }
  coordIndex IS	coordIndex
 }
}
]
}

Group { children []}
] 
}
}

##########################
#------ ACTUAL HUD ------#
##########################

HUD {
	children [
		#----------------------------#
		#------ MAIN BOX GROUP ------#
		#----------------------------#
		Group { children [ DEF ONE Box_Navigation { translation -.186 .115 -.3 diffuseColor 0 0 .5 string "Hide" box 1 whichChoice 0} DEF T1 TouchSensor { enabled TRUE }]}
		Group { children [ DEF TWO Box_Navigation { translation -.186 .097 -.3 diffuseColor .5 0 0 string "Object Size" box 2 whichChoice 0} DEF T2 TouchSensor { enabled TRUE }]}
		Group { children [ DEF THR Box_Navigation { translation -.186 .079 -.3 diffuseColor .5 0 0 string "Viewpoints" box 2 whichChoice 0} DEF T3 TouchSensor { enabled TRUE }]}
		Group { children [ DEF FOU Box_Navigation { translation -.186 .061 -.3 diffuseColor .5 0 0 string "Background" box 2 whichChoice 0} DEF T4 TouchSensor { enabled TRUE }]}
		Group { children [ DEF FIV Box_Navigation { translation -.186 .043 -.3 diffuseColor .5 0 0 string "Box Color" box 2 whichChoice 0} DEF T5 TouchSensor { enabled TRUE }]}
		#Anchor { url "http://www.badmagi.com/cgi-bin/Mall/info.pl?task=info&object=" parameter ["target=_NEW"] description "Quick Check" children [ DEF SIX Box_Navigation { translation -.186 .025 -.3 diffuseColor 0 .5 0 string "Quick Check" box 2 whichChoice 0} DEF T6 TouchSensor { enabled TRUE }]}
		#Anchor { url "http://www.badmagi.com/cgi-bin/Mall/info.pl?task=gzip&object=" parameter ["target=_NEW"] description "GZIP" children [ DEF SEV Box_Navigation { translation -.186 .007 -.3 diffuseColor 0 .5 0 string "GZip" box 2 whichChoice 0} DEF T7 TouchSensor { enabled TRUE }]}
		#Anchor { url "http://www.badmagi.com/cgi-bin/Mall/info.pl?task=help&object=" parameter ["target=_NEW"] description "Help" children [ DEF EIG Box_Navigation { translation -.186 -.011 -.3 diffuseColor .3 .3 .3 string "HELP" box 2 whichChoice 0} DEF T8 TouchSensor { enabled TRUE }]}
		#-----------------------------------------#
		#------ FANCY LINES CONNECTING BOXES -----#
		#-----------------------------------------#
		DEF NIN Lines	{ point	[-.186 .115 -.301, -.186 -.011 -.301] coordIndex [0, 1, -1] whichChoice 0}
		DEF ONE_EIT Lines	{ point	[-.186 .097 -.301, -.139 .097 -.301, -.139 .029 -.301, -.139 .065 -.301, -.139 .047 -.301, -.096 .065 -.301, -.096 .047 -.301, -.096 .029 -.301] coordIndex [0, 1, -1, 1, 2, -1, 3, 5, -1, 4, 6, -1, 2, 7, -1] whichChoice 1}
		DEF ONE_NIT Lines	{ point	[-.096 .065 -.301, -.058 .065 -.301, -.058 .108 -.301, -.058 0 -.301, -.016 .108 -.301, -.058 .09 -.301, -.016 .09 -.301, -.058 .072 -.301, -.016 .072 -.301, -.058 .054 -.301, -.016 .054 -.301, -.058 .036 -.301, -.016 .036 -.301, -.058 .018 -.301, -.016 .018 -.301, -.058 0 -.301, -.016 0 -.301] coordIndex [0, 1,-1, 2, 3 -1, 2, 4, -1, 5, 6, -1, 7, 8, -1, 9, 10, -1, 11, 12, -1, 13, 14, -1, 15, 16, -1] whichChoice 1}
		DEF ONE_TTY Lines	{ point	[-.096 .047 -.301, -.058 .047 -.301, -.058 .108 -.301, -.058 0 -.301, -.016 .108 -.301, -.058 .09 -.301, -.016 .09 -.301, -.058 .072 -.301, -.016 .072 -.301, -.058 .054 -.301, -.016 .054 -.301, -.058 .036 -.301, -.016 .036 -.301, -.058 .018 -.301, -.016 .018 -.301, -.058 0 -.301, -.016 0 -.301] coordIndex [0, 1,-1, 2, 3 -1, 2, 4, -1, 5, 6, -1, 7, 8, -1, 9, 10, -1, 11, 12, -1, 13, 14, -1, 15, 16, -1] whichChoice 1}
		DEF TWO_FOU Lines { point [-.186 .079 -.301, -.139 .079 -.301, -.139 .029 -.301, -.139 .065 -.301, -.096 .065 -.301 -.139 .047 -.301, -.096 .047 -.301, -.139 .029 -.301, -.096 .029 -.301] coordIndex [0, 1, -1, 1, 2, -1, 3, 4, -1, 5, 6, -1, 7, 8, -1] whichChoice 1}
		DEF THR_SEV Lines { point [-.186 .061 -.301, -.139 .061 -.301, -.139 .029 -.301, -.139 .065 -.301, -.096 .065 -.301 -.139 .047 -.301, -.096 .047 -.301, -.139 .029 -.301, -.096 .029 -.301, -.139 .101 -.301, -.096 .101 -.301, -.139 .083 -.301, -.096 .083 -.301, -.139 .011 -.301, -.096, .011 -.301] coordIndex [0, 1, -1, 3, 4, -1, 5, 6, -1, 7, 8, -1, 9, 10, -1, 11, 12, -1, 13, 14, -1, 9, 13, -1] whichChoice 1}
		DEF FOU_SEV Lines { point [-.186 .043 -.301, -.139 .043 -.301, -.139 .029 -.301, -.139 .065 -.301, -.096 .065 -.301 -.139 .047 -.301, -.096 .047 -.301, -.139 .029 -.301, -.096 .029 -.301, -.139 .101 -.301, -.096 .101 -.301, -.139 .083 -.301, -.096 .083 -.301, -.139 .011 -.301, -.096, .011 -.301] coordIndex [0, 1, -1, 3, 4, -1, 5, 6, -1, 7, 8, -1, 9, 10, -1, 11, 12, -1, 13, 14, -1, 9, 13, -1] whichChoice 1}
		#-----------------------------#
		#------ OBJECT SIZE CAT ------#
		#-----------------------------#
		Group { children [ DEF ONE_ONE Box_Navigation { translation -.096 .065 -.3 diffuseColor 0 .5 0 string "Normal" box 1 whichChoice 1} DEF T1_1 TouchSensor { enabled TRUE }]}
		Group { children [ DEF ONE_TWO Box_Navigation { translation -.096 .047 -.3 diffuseColor .5 0 0 string "Large" box 1 whichChoice 1} DEF T1_2 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_THR Box_Navigation { translation -.096 .029 -.3 diffuseColor 0 0 .5 string "Close Menu" box 1 whichChoice 1} DEF T1_3 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_FOU Box_Navigation { translation -.016 .108 -.3 diffuseColor 0 .5 0 string "Floor" box 1 whichChoice 1} DEF T1_4 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_FIV Box_Navigation { translation -.016 .09 -.3 diffuseColor .5 0 0 string "Back Wall" box 1 whichChoice 1} DEF T1_5 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_SIX Box_Navigation { translation -.016 .072 -.3 diffuseColor .5 0 0 string "Front Wall" box 1 whichChoice 1} DEF T1_6 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_SEV Box_Navigation { translation -.016 .054 -.3 diffuseColor .5 0 0 string "Left Wall" box 1 whichChoice 1} DEF T1_7 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_EIG Box_Navigation { translation -.016 .036 -.3 diffuseColor .5 0 0 string "Right Wall" box 1 whichChoice 1} DEF T1_8 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_NIN Box_Navigation { translation -.016 .018 -.3 diffuseColor .5 0 0 string "Ceiling" box 1 whichChoice 1} DEF T1_9 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_TEN Box_Navigation { translation -.016 0 -.3 diffuseColor 0 0 .5 string "Close Menu" box 1 whichChoice 1} DEF T1_10 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_ELE Box_Navigation { translation -.016 .108 -.3 diffuseColor 0 .5 0 string "Floor" box 1 whichChoice 1} DEF T1_11 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_TWE Box_Navigation { translation -.016 .09 -.3 diffuseColor .5 0 0 string "Back Wall" box 1 whichChoice 1} DEF T1_12 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_THI Box_Navigation { translation -.016 .072 -.3 diffuseColor .5 0 0 string "Front Wall" box 1 whichChoice 1} DEF T1_13 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_FOT Box_Navigation { translation -.016 .054 -.3 diffuseColor .5 0 0 string "Left Wall" box 1 whichChoice 1} DEF T1_14 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_FIT Box_Navigation { translation -.016 .036 -.3 diffuseColor .5 0 0 string "Right Wall" box 1 whichChoice 1} DEF T1_15 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_SIT Box_Navigation { translation -.016 .018 -.3 diffuseColor .5 0 0 string "Ceiling" box 1 whichChoice 1} DEF T1_16 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF ONE_SET Box_Navigation { translation -.016 0 -.3 diffuseColor 0 0 .5 string "Close Menu" box 1 whichChoice 1} DEF T1_17 TouchSensor { enabled TRUE  }]}
		#---------------------------#
		#------ VIEWPOINT CAT ------#
		#---------------------------#
		Group { children [ DEF TWO_ONE Box_Navigation { translation -.096 .065 -.3 diffuseColor .5 0 0 string "Default" box 1 whichChoice 1} DEF T2_1 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF TWO_TWO Box_Navigation { translation -.096 .047 -.3 diffuseColor .5 0 0 string "Floor" box 1 whichChoice 1} DEF T2_2 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF TWO_THR Box_Navigation { translation -.096 .029 -.3 diffuseColor 0 0 .5 string "Close Menu" box 1 whichChoice 1} DEF T2_3 TouchSensor { enabled TRUE  }]}
		#------------------------------#								
		#------ BACKGROUND COLOR ------#
		#------------------------------#
		Group { children [ DEF THR_ONE Box_Navigation { translation -.096 .101 -.3 diffuseColor .5 0 0 string "Black" box 1 whichChoice 1} DEF T3_1 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF THR_TWO Box_Navigation { translation -.096 .083 -.3 diffuseColor .5 0 0 string "Red" box 1 whichChoice 1} DEF T3_2 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF THR_THR Box_Navigation { translation -.096 .065 -.3 diffuseColor .5 0 0 string "Green" box 1 whichChoice 1} DEF T3_3 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF THR_FOU Box_Navigation { translation -.096 .047 -.3 diffuseColor .5 0 0 string "Blue" box 1 whichChoice 1} DEF T3_4 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF THR_FIV Box_Navigation { translation -.096 .029 -.3 diffuseColor .5 0 0 string "White" box 1 whichChoice 1} DEF T3_5 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF THR_SIX Box_Navigation { translation -.096 .011 -.3 diffuseColor 0 0 .5 string "Close Menu" box 1 whichChoice 1} DEF T3_6 TouchSensor { enabled TRUE  }]}
		#-----------------------#
		#------ BOX COLOR ------#
		#-----------------------#
		Group { children [ DEF FOU_ONE Box_Navigation { translation -.096 .101 -.3 diffuseColor .5 0 0 string "Black" box 1 whichChoice 1} DEF T4_1 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF FOU_TWO Box_Navigation { translation -.096 .083 -.3 diffuseColor .5 0 0 string "Red" box 1 whichChoice 1} DEF T4_2 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF FOU_THR Box_Navigation { translation -.096 .065 -.3 diffuseColor .5 0 0 string "Green" box 1 whichChoice 1} DEF T4_3 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF FOU_FOU Box_Navigation { translation -.096 .047 -.3 diffuseColor .5 0 0 string "Blue" box 1 whichChoice 1} DEF T4_4 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF FOU_FIV Box_Navigation { translation -.096 .029 -.3 diffuseColor .5 0 0 string "White" box 1 whichChoice 1} DEF T4_5 TouchSensor { enabled TRUE  }]}
		Group { children [ DEF FOU_SIX Box_Navigation { translation -.096 .011 -.3 diffuseColor 0 0 .5 string "Close Menu" box 1 whichChoice 1} DEF T4_6 TouchSensor { enabled TRUE  }]}
	]
}

##################################
#------ ALL PURPOSE SCRIPT ------#
##################################
DEF SCRIPT Script {
#----------------------------------------------------#
#------ LIST OF FUNCTION NAMES FOR MOUSE-OVERS ------#
#----------------------------------------------------#
	eventIn SFBool in1
	eventIn SFBool in2
	eventIn SFBool in3
	eventIn SFBool in4
	eventIn SFBool in5
	eventIn SFBool in6
	eventIn SFBool in7
	eventIn SFBool in8
	eventIn SFBool in1_1
	eventIn SFBool in1_2
	eventIn SFBool in1_3
	eventIn SFBool in1_4
	eventIn SFBool in1_5
	eventIn SFBool in1_6
	eventIn SFBool in1_7
	eventIn SFBool in1_8
	eventIn SFBool in1_9
	eventIn SFBool in1_10
	eventIn SFBool in1_11
	eventIn SFBool in1_12
	eventIn SFBool in1_13
	eventIn SFBool in1_14
	eventIn SFBool in1_15
	eventIn SFBool in1_16
	eventIn SFBool in1_17
	eventIn SFBool in1_18
	eventIn SFBool in1_19
	eventIn SFBool in1_20
	eventIn SFBool in2_1
	eventIn SFBool in2_2
	eventIn SFBool in2_3
	eventIn SFBool in2_4
	eventIn SFBool in2_5
	eventIn SFBool in3_1
	eventIn SFBool in3_2
	eventIn SFBool in3_3
	eventIn SFBool in3_4
	eventIn SFBool in3_5
	eventIn SFBool in3_6
	eventIn SFBool in3_7
    eventIn SFBool in4_1
	eventIn SFBool in4_2
	eventIn SFBool in4_3
	eventIn SFBool in4_4
	eventIn SFBool in4_5
	eventIn SFBool in4_6
	eventIn SFBool in4_7

#-------------------------------------------#
#------ OUTPUT COLORS FOR MOUSE-OVERS ------#
#-------------------------------------------#
	eventOut SFColor out1
	eventOut SFColor out2
	eventOut SFColor out3
	eventOut SFColor out4
	eventOut SFColor out5
	eventOut SFColor out6
	eventOut SFColor out7
	eventOut SFColor out8
	eventOut SFColor out1_1
	eventOut SFColor out1_2
	eventOut SFColor out1_3
	eventOut SFColor out1_4
	eventOut SFColor out1_5
	eventOut SFColor out1_6
	eventOut SFColor out1_7
	eventOut SFColor out1_8
	eventOut SFColor out1_9
	eventOut SFColor out1_10
	eventOut SFColor out1_11
	eventOut SFColor out1_12
	eventOut SFColor out1_13
	eventOut SFColor out1_14
	eventOut SFColor out1_15
	eventOut SFColor out1_16
	eventOut SFColor out1_17
	eventOut SFColor out1_18
	eventOut SFColor out1_19
	eventOut SFColor out1_20
	eventOut SFColor out2_1
	eventOut SFColor out2_2
	eventOut SFColor out2_3
	eventOut SFColor out2_4
	eventOut SFColor out2_5
	eventOut SFColor out3_1
	eventOut SFColor out3_2
	eventOut SFColor out3_3
	eventOut SFColor out3_4
	eventOut SFColor out3_5
	eventOut SFColor out3_6
	eventOut SFColor out3_7
    eventOut SFColor out4_1
	eventOut SFColor out4_2
	eventOut SFColor out4_3
	eventOut SFColor out4_4
	eventOut SFColor out4_5
	eventOut SFColor out4_6
	eventOut SFColor out4_7

#---------------------------------------#
#------ CLICK FUNCTIONS FOR BOXES ------#
#---------------------------------------#	
eventIn SFTime click1 
eventIn SFTime click2 
eventIn SFTime click3 
eventIn SFTime click4 
eventIn SFTime click5 
eventIn SFTime click6 
eventIn SFTime click7 
eventIn SFTime click8 
eventIn SFTime click1_1 
eventIn SFTime click1_2 
eventIn SFTime click1_3 
eventIn SFTime click1_4 
eventIn SFTime click1_5 
eventIn SFTime click1_6 
eventIn SFTime click1_7 
eventIn SFTime click1_8 
eventIn SFTime click1_9 
eventIn SFTime click1_10 
eventIn SFTime click1_11 
eventIn SFTime click1_12 
eventIn SFTime click1_13 
eventIn SFTime click1_14 
eventIn SFTime click1_15 
eventIn SFTime click1_16 
eventIn SFTime click1_17 
eventIn SFTime click1_18 
eventIn SFTime click1_19 
eventIn SFTime click1_20 
eventIn SFBool click2_1 
eventIn SFBool click2_2 
eventIn SFTime click2_3 
eventIn SFTime click2_4 
eventIn SFTime click2_5 
eventIn SFTime click3_1 
eventIn SFTime click3_2 
eventIn SFTime click3_3 
eventIn SFTime click3_4 
eventIn SFTime click3_5 
eventIn SFTime click3_6 
eventIn SFTime click3_7 
eventIn SFTime click4_1 
eventIn SFTime click4_2 
eventIn SFTime click4_3 
eventIn SFTime click4_4 
eventIn SFTime click4_5 
eventIn SFTime click4_6 
eventIn SFTime click4_7 
	eventIn SFTime click_final

	# FOR BACKGROUND COLOR #
	eventIn SFTime color_change
	eventOut SFColor diffuseColor
	eventOut MFColor skyColor

#-------------------------------------------------------#
#------ OUTPUTS FOR WHETHER A BOX IS HIDDEN/SHOWN ------#
#-------------------------------------------------------#
eventOut SFInt32 whichChoice1 
eventOut SFInt32 whichChoice2 
eventOut SFInt32 whichChoice3 
eventOut SFInt32 whichChoice4 
eventOut SFInt32 whichChoice5 
eventOut SFInt32 whichChoice6 
eventOut SFInt32 whichChoice7 
eventOut SFInt32 whichChoice8 
eventOut SFInt32 whichChoice9
eventOut SFInt32 whichChoice1_1 
eventOut SFInt32 whichChoice1_2 
eventOut SFInt32 whichChoice1_3 
eventOut SFInt32 whichChoice1_4 
eventOut SFInt32 whichChoice1_5 
eventOut SFInt32 whichChoice1_6 
eventOut SFInt32 whichChoice1_7 
eventOut SFInt32 whichChoice1_8 
eventOut SFInt32 whichChoice1_9 
eventOut SFInt32 whichChoice1_10 
eventOut SFInt32 whichChoice1_11 
eventOut SFInt32 whichChoice1_12 
eventOut SFInt32 whichChoice1_13 
eventOut SFInt32 whichChoice1_14 
eventOut SFInt32 whichChoice1_15 
eventOut SFInt32 whichChoice1_16 
eventOut SFInt32 whichChoice1_17 
eventOut SFInt32 whichChoice1_18 
eventOut SFInt32 whichChoice1_19 
eventOut SFInt32 whichChoice1_20 
eventOut SFInt32 whichChoice2_1 
eventOut SFInt32 whichChoice2_2 
eventOut SFInt32 whichChoice2_3 
eventOut SFInt32 whichChoice2_4 
eventOut SFInt32 whichChoice2_5 
eventOut SFInt32 whichChoice3_1 
eventOut SFInt32 whichChoice3_2 
eventOut SFInt32 whichChoice3_3 
eventOut SFInt32 whichChoice3_4 
eventOut SFInt32 whichChoice3_5 
eventOut SFInt32 whichChoice3_6 
eventOut SFInt32 whichChoice3_7 
eventOut SFInt32 whichChoice4_1 
eventOut SFInt32 whichChoice4_2 
eventOut SFInt32 whichChoice4_3 
eventOut SFInt32 whichChoice4_4 
eventOut SFInt32 whichChoice4_5 
eventOut SFInt32 whichChoice4_6 
eventOut SFInt32 whichChoice4_7

#-------------------------------#
#------ BOX AROUND OBJECT ------#
#-------------------------------#
eventOut SFInt32 whichChoiceFLOOR
field SFInt32 FLOOR 0
eventOut SFInt32 whichChoiceRWALL
field SFInt32 RWALL 1
eventOut SFInt32 whichChoiceLWALL
field SFInt32 LWALL 1
eventOut SFInt32 whichChoiceBWALL
field SFInt32 BWALL 1
eventOut SFInt32 whichChoiceFWALL
field SFInt32 FWALL 1
eventOut SFInt32 whichChoiceROOF
field SFInt32 ROOF 1

eventOut SFVec3f translationFLOOR
eventOut SFVec3f translationRWALL
eventOut SFVec3f translationLWALL
eventOut SFVec3f translationBWALL
eventOut SFVec3f translationFWALL
eventOut SFVec3f translationROOF
eventOut SFVec3f sizeFLOOR
eventOut SFVec3f sizeRWALL
eventOut SFVec3f sizeLWALL
eventOut SFVec3f sizeBWALL
eventOut SFVec3f sizeFWALL
eventOut SFVec3f sizeROOF
eventOut SFColor colorFLOOR
eventOut SFColor colorRWALL
eventOut SFColor colorLWALL
eventOut SFColor colorBWALL
eventOut SFColor colorFWALL
eventOut SFColor colorROOF

field SFColor FLOORC .0 .5 0
field SFColor RWALLC .5 0 0
field SFColor LWALLC .5 0 0
field SFColor BWALLC .5 0 0
field SFColor FWALLC .5 0 0
field SFColor ROOFC .5 0 0
field SFColor DEFC 0 .5 0
field SFColor LARC .5 0 0
field SFColor FLOORCO 0 1 0
field SFColor RWALLCO 1 0 0
field SFColor LWALLCO 1 0 0
field SFColor BWALLCO 1 0 0
field SFColor FWALLCO 1 0 0
field SFColor ROOFCO 1 0 0
field SFColor DEFCO 0 1 0
field SFColor LARCO 0 1 0

eventIn SFBool PLATFORM_FINAL
eventIn SFBool box_color

		  

#-----------------------------#
#------	OTHER VARIABLES ------#
#-----------------------------#
field SFInt32 hide 1
eventOut MFString text
field SFBool boolValue TRUE
  eventOut SFBool output
    eventOut SFBool output2
eventOut SFVec3f position

	url	"javascript: 
   //
   // FUNCTIONS DEALING WITH MOUSE-OVERS
   // 
	function in1(value, timestamp) {if (value) {out1[0] = 0; out1[1] = 0; out1[2] = 1;} else {out1[0] = 0; out1[1] = 0; out1[2] = .5;}}
	function in2(value, timestamp) {if (value) {out2[0] = 1; out2[1] = 0; out2[2] = 0;} else {out2[0] = 0.5; out2[1] = 0; out2[2] = 0;}}
   	function in3(value, timestamp) {if (value) {out3[0] = 1; out3[1] = 0; out3[2] = 0;} else {out3[0] = 0.5; out3[1] = 0; out3[2] = 0;}}
	function in4(value, timestamp) {if (value) {out4[0] = 1; out4[1] = 0; out4[2] = 0;} else {out4[0] = 0.5; out4[1] = 0; out4[2] = 0;}}
	function in5(value, timestamp) {if (value) {out5[0] = 1; out5[1] = 0; out5[2] = 0;} else {out5[0] = 0.5; out5[1] = 0; out5[2] = 0;}} 
function in6(value, timestamp) {if (value) {out6[0] = 0; out6[1] = 1; out6[2] = 0;} else {out6[0] = 0; out6[1] = .5; out6[2] = 0;}} 
function in7(value, timestamp) {if (value) {out7[0] = 0; out7[1] = 1; out7[2] = 0;} else {out7[0] = 0; out7[1] = .5; out7[2] = 0;}} 
function in8(value, timestamp) {if (value) {out8[0] = .7; out8[1] = .7; out8[2] = .7;} else {out8[0] = .3; out8[1] = .3; out8[2] = .3;}} 
function in1_1(value, timestamp) {if (value) {out1_1 = DEFCO;} else {out1_1 = DEFC;}} 
function in1_2(value, timestamp) {if (value) {out1_2 = LARCO;} else {out1_2 = LARC;}} 
function in1_3(value, timestamp) {if (value) {out1_3[0] = 0; out1_3[1] = 0; out1_3[2] = 1;} else {out1_3[0] = 0; out1_3[1] = 0; out1_3[2] = .5;}} 
function in1_4(value, timestamp) {if (value) {out1_4 = FLOORCO;} else {out1_4 = FLOORC;}} 
function in1_5(value, timestamp) {if (value) {out1_5 = BWALLCO;} else {out1_5 = BWALLC;}} 
function in1_6(value, timestamp) {if (value) {out1_6 = FWALLCO;} else {out1_6 = FWALLC;}} 
function in1_7(value, timestamp) {if (value) {out1_7 = LWALLCO;} else {out1_7 = LWALLC;}} 
function in1_8(value, timestamp) {if (value) {out1_8 = RWALLCO;} else {out1_8 = RWALLC;}} 
function in1_9(value, timestamp) {if (value) {out1_9 = ROOFCO;} else {out1_9 = ROOFC;}} 
function in1_10(value, timestamp) {if (value) {out1_10[0] = 0; out1_10[1] = 0; out1_10[2] = 1;} else {out1_10[0] = 0; out1_10[1] = 0; out1_10[2] = .5;}} 
function in1_11(value, timestamp) {if (value) {out1_11 = FLOORCO;} else {out1_11 = FLOORC;}} 
function in1_12(value, timestamp) {if (value) {out1_12 = BWALLCO;} else {out1_12 = BWALLC;}} 
function in1_13(value, timestamp) {if (value) {out1_13 = FWALLCO;} else {out1_13 = FWALLC;}} 
function in1_14(value, timestamp) {if (value) {out1_14 = LWALLCO;} else {out1_14 = LWALLC;}} 
function in1_15(value, timestamp) {if (value) {out1_15 = RWALLCO;} else {out1_15 = RWALLC;}} 
function in1_16(value, timestamp) {if (value) {out1_16 = ROOFCO;} else {out1_16 = ROOFC;}} 
function in1_17(value, timestamp) {if (value) {out1_17[0] = 0; out1_17[1] = 0; out1_17[2] = 1;} else {out1_17[0] = 0; out1_17[1] = 0; out1_17[2] = .5;}} 
function in1_18(value, timestamp) {if (value) {out1_18[0] = 1; out1_18[1] = 0; out1_18[2] = 0;} else {out1_18[0] = 0.5; out1_18[1] = 0; out1_18[2] = 0;}} 
function in1_19(value, timestamp) {if (value) {out1_19[0] = 1; out1_19[1] = 0; out1_19[2] = 0;} else {out1_19[0] = 0.5; out1_19[1] = 0; out1_19[2] = 0;}} 
function in1_20(value, timestamp) {if (value) {out1_20[0] = 1; out1_20[1] = 0; out1_20[2] = 0;} else {out1_20[0] = 0.5; out1_20[1] = 0; out1_20[2] = 0;}} 
function in2_1(value, timestamp) {if (value) {out2_1[0] = 1; out2_1[1] = 0; out2_1[2] = 0;} else {out2_1[0] = 0.5; out2_1[1] = 0; out2_1[2] = 0;}} 
function in2_2(value, timestamp) {if (value) {out2_2[0] = 1; out2_2[1] = 0; out2_2[2] = 0;} else {out2_2[0] = 0.5; out2_2[1] = 0; out2_2[2] = 0;}} 
function in2_3(value, timestamp) {if (value) {out2_3[0] = 0; out2_3[1] = 0; out2_3[2] = 1;} else {out2_3[0] = 0; out2_3[1] = 0; out2_3[2] = .5;}} 
function in2_4(value, timestamp) {if (value) {out2_4[0] = 1; out2_4[1] = 0; out2_4[2] = 0;} else {out2_4[0] = 0.5; out2_4[1] = 0; out2_4[2] = 0;}} 
function in2_5(value, timestamp) {if (value) {out2_5[0] = 1; out2_5[1] = 0; out2_5[2] = 0;} else {out2_5[0] = 0.5; out2_5[1] = 0; out2_5[2] = 0;}} 
function in3_1(value, timestamp) {if (value) {out3_1[0] = 1; out3_1[1] = 0; out3_1[2] = 0;} else {out3_1[0] = 0.5; out3_1[1] = 0; out3_1[2] = 0;}} 
function in3_2(value, timestamp) {if (value) {out3_2[0] = 1; out3_2[1] = 0; out3_2[2] = 0;} else {out3_2[0] = 0.5; out3_2[1] = 0; out3_2[2] = 0;}} 
function in3_3(value, timestamp) {if (value) {out3_3[0] = 1; out3_3[1] = 0; out3_3[2] = 0;} else {out3_3[0] = 0.5; out3_3[1] = 0; out3_3[2] = 0;}} 
function in3_4(value, timestamp) {if (value) {out3_4[0] = 1; out3_4[1] = 0; out3_4[2] = 0;} else {out3_4[0] = 0.5; out3_4[1] = 0; out3_4[2] = 0;}} 
function in3_5(value, timestamp) {if (value) {out3_5[0] = 1; out3_5[1] = 0; out3_5[2] = 0;} else {out3_5[0] = 0.5; out3_5[1] = 0; out3_5[2] = 0;}} 
function in3_6(value, timestamp) {if (value) {out3_6[0] = 0; out3_6[1] = 0; out3_6[2] = 1;} else {out3_6[0] = 0; out3_6[1] = 0; out3_6[2] = 0.5;}} 
function in3_7(value, timestamp) {if (value) {out3_7[0] = 1; out3_7[1] = 0; out3_7[2] = 0;} else {out3_7[0] = 0.5; out3_7[1] = 0; out3_7[2] = 0;}} 
function in4_1(value, timestamp) {if (value) {out4_1[0] = 1; out4_1[1] = 0; out4_1[2] = 0;} else {out4_1[0] = 0.5; out4_1[1] = 0; out4_1[2] = 0;}} 
function in4_2(value, timestamp) {if (value) {out4_2[0] = 1; out4_2[1] = 0; out4_2[2] = 0;} else {out4_2[0] = 0.5; out4_2[1] = 0; out4_2[2] = 0;}} 
function in4_3(value, timestamp) {if (value) {out4_3[0] = 1; out4_3[1] = 0; out4_3[2] = 0;} else {out4_3[0] = 0.5; out4_3[1] = 0; out4_3[2] = 0;}} 
function in4_4(value, timestamp) {if (value) {out4_4[0] = 1; out4_4[1] = 0; out4_4[2] = 0;} else {out4_4[0] = 0.5; out4_4[1] = 0; out4_4[2] = 0;}} 
function in4_5(value, timestamp) {if (value) {out4_5[0] = 1; out4_5[1] = 0; out4_5[2] = 0;} else {out4_5[0] = 0.5; out4_5[1] = 0; out4_5[2] = 0;}} 
function in4_6(value, timestamp) {if (value) {out4_6[0] = 0; out4_6[1] = 0; out4_6[2] = 1;} else {out4_6[0] = 0; out4_6[1] = 0; out4_6[2] = 0.5;}} 
function in4_7(value, timestamp) {if (value) {out4_7[0] = 1; out4_7[1] = 0; out4_7[2] = 0;} else {out4_7[0] = 0.5; out4_7[1] = 0; out4_7[2] = 0;}} 

//
// FUNCTIONS DEALING WITH MENU HIDING/SHOWING
//

function click1() { 
	if(hide==1) {
	hide = 2;
	text = 'Show';
	click_final(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
} else {
	hide = 1;
	text = 'Hide';
	click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
}
}	
    function click2() { click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);}	
  function click1_1() { click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1); PLATFORM_FINAL(6);}
  function click1_2() { click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1); PLATFORM_FINAL(7);}
  function click1_3() { click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);}
  function click1_4() { PLATFORM_FINAL(0, 0);}
  function click1_5() { PLATFORM_FINAL(3, 0);}
  function click1_6() { PLATFORM_FINAL(4, 0);}
  function click1_7() { PLATFORM_FINAL(2, 0);}
  function click1_8() { PLATFORM_FINAL(1, 0);}
  function click1_9() { PLATFORM_FINAL(5, 0);}
 function click1_10() { click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);}
   function click1_11() { PLATFORM_FINAL(0, 1);}
  function click1_12() { PLATFORM_FINAL(3, 1);}
  function click1_13() { PLATFORM_FINAL(4, 1);}
  function click1_14() { PLATFORM_FINAL(2, 1);}
  function click1_15() { PLATFORM_FINAL(1, 1);}
  function click1_16() { PLATFORM_FINAL(5, 1);}
 function click1_17() { click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);}
 function click2_1(value, time) {
         if (value==boolValue) output = value;
      }
 function click2_2(value, time) {
         if (value==boolValue) output2 = value;
      }
 function click2_3() {  click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);}
 function click3() {	click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);}
 function click3_1() {	color_change(0); diffuseColor = '1 1 1';}
 function click3_2() { color_change(1); diffuseColor = '1 1 1'; }
 function click3_3() { color_change(2); diffuseColor = '1 0 0';}
 function click3_4() { color_change(3); diffuseColor = '1 1 1';}
 function click3_5() { color_change(4); diffuseColor = '0 0 0';}
function click3_6() {	click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);}
 function click4() {	click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1);}
 function click4_1() { box_color('0 0 0');}
 function click4_2() { box_color('1 0 0');}
 function click4_3() { box_color('0 1 0');}
 function click4_4() { box_color('0 0 1');}
 function click4_5() { box_color('1 1 1');}
function click4_6() {	click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);}
 function click5() {	click_final(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0);}
 function click_final(c1, c2, c3, c4, c5, c6, c7, c8, c9, c1_1, c1_2, c1_3, c1_4, c1_5, c1_6, c1_7, c1_8, c1_9, c1_10, c1_11, c1_12, c1_13, c1_14, c1_15, c1_16, c1_17, c1_18, c1_19, c1_20, c2_1, c2_2, c2_3, c2_4, c2_5, c3_1, c3_2, c3_3, c3_4, c3_5, c3_6, c3_7, c4_1, c4_2, c4_3, c4_4, c4_5, c4_6, c4_7) { whichChoice1 = c1; whichChoice2 = c2; whichChoice3 = c3; whichChoice4 = c4; whichChoice5 = c5; whichChoice6 = c6; whichChoice7 = c7; whichChoice8 = c8; whichChoice1_1 = c1_1; whichChoice1_2 = c1_2; whichChoice1_3 = c1_3; whichChoice1_4 = c1_4; whichChoice1_5 = c1_5; whichChoice1_6 = c1_6; whichChoice1_7 = c1_7; whichChoice1_8 = c1_8; whichChoice1_9 = c1_9; whichChoice1_10 = c1_10; whichChoice1_11 = c1_11; whichChoice1_12 = c1_12; whichChoice1_13 = c1_13; whichChoice1_14 = c1_14; whichChoice1_15 = c1_15; whichChoice1_16 = c1_16; whichChoice1_17 = c1_17; whichChoice1_18 = c1_18; whichChoice1_19 = c1_19; whichChoice1_20 = c1_20; whichChoice2_1 = c2_1; whichChoice2_2 = c2_2; whichChoice2_3 = c2_3; whichChoice2_4 = c2_4; whichChoice2_5 = c2_5; whichChoice3_1 = c3_1; whichChoice3_2 = c3_2; whichChoice3_3 = c3_3; whichChoice3_4 = c3_4; whichChoice3_5 = c3_5; whichChoice3_6 = c3_6; whichChoice3_7 = c3_7; whichChoice4_1 = c4_1; whichChoice4_2 = c4_2; whichChoice4_3 = c4_3; whichChoice4_4 = c4_4; whichChoice4_5 = c4_5; whichChoice4_6 = c4_6; whichChoice4_7 = c4_7; whichChoice9 = c9; }
//
// CHANGING BACKGROUND COLOR
//
 function color_change(one) {
	 if(one==0) skyColor = '0 0 0';
	 if(one==1) skyColor = '1 0 0';
	 if(one==2) skyColor = '0 1 0';
	 if(one==3) skyColor = '0 0 1';
	 if(one==4) skyColor = '1 1 1';
 }

 function box_color(value) {
  colorFLOOR = value;
  colorRWALL = value;
  colorLWALL = value;
  colorFWALL = value;
  colorBWALL = value;
  colorROOF = value;
 }

 function PLATFORM_FINAL(value, value2) {
	 // FLOOR
	 if(value==0) {
	 	  if(FLOOR==0) {
		  whichChoiceFLOOR = 1;
		  out1_4 = '.5 0 0';
		  out1_11 = '.5 0 0';
		  FLOORCO = '1 0 0';
		  FLOORC = '.5 0 0';
		  FLOOR = 1; 
	  } else {
		  if(value2==0) {
		  whichChoiceFLOOR = 0;
	  } else {
		  whichChoiceFLOOR = 2;
	  }
		  out1_4 = '0 .5 0';
		  out1_11 = '0 .5 0';
		  FLOORCO = '0 1 0';
		  FLOORC = '0 .5 0';
		  FLOOR = 0;
	  }
  }
  // RWALL
	 if(value==1) {
	 	  if(RWALL==0) {
		  whichChoiceRWALL = 1;
		  out1_8 = '.5 0 0';
		  out1_15 = '.5 0 0';
		  RWALLCO = '1 0 0';
		  RWALLC = '.5 0 0';
		  RWALL = 1;
	  } else {
		  if(value2==0) {
		  whichChoiceRWALL = 0;
	  } else {
		  whichChoiceRWALL = 2;
	  }
		  out1_8 = '0 .5 0';
		  out1_15 = '0 .5 0';
		  RWALLCO = '0 1 0';
		  RWALLC = '0 .5 0';
		  RWALL = 0;
	  }
  }
  // LWALL
  	 if(value==2) {
	 	  if(LWALL==0) {
		  whichChoiceLWALL = 1;
		  out1_7 = '.5 0 0';
		  out1_14 = '.5 0 0';
		  LWALLCO = '1 0 0';
		  LWALLC = '.5 0 0';
          LWALL = 1;
	  } else {
		  if(value2==0) {
		  whichChoiceLWALL = 0;
	  } else {
		  whichChoiceLWALL = 2;
	  }
		  out1_7 = '0 .5 0';
		  out1_14 = '0 .5 0';
		  LWALLCO = '0 1 0';
		  LWALLC = '0 .5 0';
		  LWALL = 0;
	  }
  }
  // BWALL
    	 if(value==3) {
	 	  if(BWALL==0) {
		  whichChoiceBWALL = 1;
		  out1_5 = '.5 0 0';
		  out1_12 = '.5 0 0';
		  BWALLCO = '1 0 0';
		  BWALLC = '.5 0 0';
		  BWALL = 1;
	  } else {
		  if(value2==0) {
		  whichChoiceBWALL = 0;
	  } else {
		  whichChoiceBWALL = 2;
	  }
		  out1_5 = '0 .5 0';
		  out1_12 = '0 .5 0';
		  BWALLCO = '0 1 0';
		  BWALLC = '0 .5 0';
		  BWALL = 0;
	  }
  }
  // FWALL 
      	 if(value==4) {
	 	  if(FWALL==0) {
		  whichChoiceFWALL = 1;
		  out1_6 = '.5 0 0';
		  out1_13 = '.5 0 0';
		  FWALLCO = '1 0 0';
		  FWALLC = '.5 0 0';
		  FWALL = 1;
	  } else {
		  if(value2==0) {
		  whichChoiceFWALL = 0;
	  } else {
		  whichChoiceFWALL = 2;
	  }
		  out1_6 = '0 .5 0';
		  out1_13 = '0 .5 0';
		  FWALLCO = '0 1 0';
		  FWALLC = '0 .5 0';
		  FWALL = 0;
	  }
  }
  // ROOF
        	 if(value==5) {
	 	  if(ROOF==0) {
		  whichChoiceROOF = 1;
		  out1_9 = '.5 0 0';
		  out1_16 = '.5 0 0';
		  ROOFCO = '1 0 0';
		  ROOFC = '.5 0 0';
		  ROOF = 1;
	  } else {
		  if(value2==0) {
		  whichChoiceROOF = 0;
	  } else {
		  whichChoiceROOF = 2;
	  }
		  out1_9 = '0 .5 0';
		  out1_16 = '0 .5 0';
		  ROOFCO = '0 1 0';
		  ROOFC = '0 .5 0';
		  ROOF = 0;
	  }
  }
  if(value==6) {
translationRWALL = '1.5 -.25 0';
translationLWALL = '-1.5 -.25 0';
translationBWALL = '0 -.25 -1.5';
translationFWALL = '0 -.25 1.5';
translationROOF = ' 0 1.25 0';
position = '0 -1.75 3.1';
out1_1 = '0 .5 0';
out1_2 = '.5 0 0';
DEFC = '0 .5 0';
DEFCO = '0 1 0';
LARC = '.5 0 0';
LARCO = '1 0 0';
if(FLOOR==0) {
	whichChoiceFLOOR = 0;
}
if(RWALL==0) {
	whichChoiceRWALL = 0;
}
if(LWALL==0) {
	whichChoiceLWALL = 0;
}
if(BWALL==0) {
	whichChoiceBWALL = 0;
}
if(FWALL==0) {
	whichChoiceFWALL = 0;
}
if(ROOF==0) {
	whichChoiceROOF = 0;
}
}
if(value==7) {
translationRWALL = '5 3.25 0';
translationLWALL = '-5 3.25 0';
translationBWALL = '0 3.25 -5';
translationFWALL = '0 3.25 5';
translationROOF = '0 8.25 0';
position = '0 -1.75 6.6';
out1_1 = '.5 0 0';
out1_2 = '0 .5 0';
DEFC = '.5 0 0';
DEFCO = '1 0 0';
LARC = '0 .5 0';
LARCO = '0 1 0';
if(FLOOR==0) {
	whichChoiceFLOOR = 2;
}
if(RWALL==0) {
	whichChoiceRWALL = 2;
}
if(LWALL==0) {
	whichChoiceLWALL = 2;
}
if(BWALL==0) {
	whichChoiceBWALL = 2;
}
if(FWALL==0) {
	whichChoiceFWALL = 2;
}
if(ROOF==0) {
	whichChoiceROOF = 2;
}
}

}
	"
}

#################################
#------ MOUSE-OVER ROUTES ------#
#################################

ROUTE SCRIPT.text TO ONE.string
ROUTE T1.isOver	TO SCRIPT.in1
ROUTE SCRIPT.out1 TO	ONE.diffuseColor
ROUTE T2.isOver	TO SCRIPT.in2
ROUTE SCRIPT.out2 TO	TWO.diffuseColor
ROUTE T3.isOver	TO SCRIPT.in3
ROUTE SCRIPT.out3 TO	THR.diffuseColor
ROUTE T4.isOver TO SCRIPT.in4 
ROUTE SCRIPT.out4 TO FOU.diffuseColor 
ROUTE T5.isOver TO SCRIPT.in5 
ROUTE SCRIPT.out5 TO FIV.diffuseColor 
#ROUTE T6.isOver TO SCRIPT.in6 
#ROUTE SCRIPT.out6 TO SIX.diffuseColor 
#ROUTE T7.isOver TO SCRIPT.in7 
#ROUTE SCRIPT.out7 TO SEV.diffuseColor 
#ROUTE T8.isOver TO SCRIPT.in8 
#ROUTE SCRIPT.out8 TO EIG.diffuseColor 
ROUTE T1_1.isOver TO SCRIPT.in1_1 
ROUTE SCRIPT.out1_1 TO ONE_ONE.diffuseColor 
ROUTE T1_2.isOver TO SCRIPT.in1_2 
ROUTE SCRIPT.out1_2 TO ONE_TWO.diffuseColor 
ROUTE T1_3.isOver TO SCRIPT.in1_3 
ROUTE SCRIPT.out1_3 TO ONE_THR.diffuseColor 
ROUTE T1_4.isOver TO SCRIPT.in1_4 
ROUTE SCRIPT.out1_4 TO ONE_FOU.diffuseColor 
ROUTE T1_5.isOver TO SCRIPT.in1_5 
ROUTE SCRIPT.out1_5 TO ONE_FIV.diffuseColor 
ROUTE T1_6.isOver TO SCRIPT.in1_6 
ROUTE SCRIPT.out1_6 TO ONE_SIX.diffuseColor 
ROUTE T1_7.isOver TO SCRIPT.in1_7 
ROUTE SCRIPT.out1_7 TO ONE_SEV.diffuseColor 
ROUTE T1_8.isOver TO SCRIPT.in1_8 
ROUTE SCRIPT.out1_8 TO ONE_EIG.diffuseColor 
ROUTE T1_9.isOver TO SCRIPT.in1_9 
ROUTE SCRIPT.out1_9 TO ONE_NIN.diffuseColor 
ROUTE T1_10.isOver TO SCRIPT.in1_10 
ROUTE SCRIPT.out1_10 TO ONE_TEN.diffuseColor
ROUTE T1_11.isOver TO SCRIPT.in1_11 
ROUTE SCRIPT.out1_11 TO ONE_ELE.diffuseColor 
ROUTE T1_12.isOver TO SCRIPT.in1_12 
ROUTE SCRIPT.out1_12 TO ONE_TWE.diffuseColor 
ROUTE T1_13.isOver TO SCRIPT.in1_13 
ROUTE SCRIPT.out1_13 TO ONE_THI.diffuseColor 
ROUTE T1_14.isOver TO SCRIPT.in1_14 
ROUTE SCRIPT.out1_14 TO ONE_FOT.diffuseColor 
ROUTE T1_15.isOver TO SCRIPT.in1_15 
ROUTE SCRIPT.out1_15 TO ONE_FIT.diffuseColor 
ROUTE T1_16.isOver TO SCRIPT.in1_16 
ROUTE SCRIPT.out1_16 TO ONE_SIT.diffuseColor 
ROUTE T1_17.isOver TO SCRIPT.in1_17 
ROUTE SCRIPT.out1_17 TO ONE_SET.diffuseColor
ROUTE T2_1.isOver TO SCRIPT.in2_1 
ROUTE SCRIPT.out2_1 TO TWO_ONE.diffuseColor
ROUTE T2_2.isOver TO SCRIPT.in2_2 
ROUTE SCRIPT.out2_2 TO TWO_TWO.diffuseColor
ROUTE T2_3.isOver TO SCRIPT.in2_3 
ROUTE SCRIPT.out2_3 TO TWO_THR.diffuseColor
ROUTE T3_1.isOver TO SCRIPT.in3_1 
ROUTE SCRIPT.out3_1 TO THR_ONE.diffuseColor 
ROUTE T3_2.isOver TO SCRIPT.in3_2
ROUTE SCRIPT.out3_2 TO THR_TWO.diffuseColor 
ROUTE T3_3.isOver TO SCRIPT.in3_3 
ROUTE SCRIPT.out3_3 TO THR_THR.diffuseColor 
ROUTE T3_4.isOver TO SCRIPT.in3_4 
ROUTE SCRIPT.out3_4 TO THR_FOU.diffuseColor 
ROUTE T3_5.isOver TO SCRIPT.in3_5 
ROUTE SCRIPT.out3_5 TO THR_FIV.diffuseColor 
ROUTE T3_6.isOver TO SCRIPT.in3_6 
ROUTE SCRIPT.out3_6 TO THR_SIX.diffuseColor
ROUTE T4_1.isOver TO SCRIPT.in4_1 
ROUTE SCRIPT.out4_1 TO FOU_ONE.diffuseColor 
ROUTE T4_2.isOver TO SCRIPT.in4_2
ROUTE SCRIPT.out4_2 TO FOU_TWO.diffuseColor 
ROUTE T4_3.isOver TO SCRIPT.in4_3 
ROUTE SCRIPT.out4_3 TO FOU_THR.diffuseColor 
ROUTE T4_4.isOver TO SCRIPT.in4_4 
ROUTE SCRIPT.out4_4 TO FOU_FOU.diffuseColor 
ROUTE T4_5.isOver TO SCRIPT.in4_5 
ROUTE SCRIPT.out4_5 TO FOU_FIV.diffuseColor 
ROUTE T4_6.isOver TO SCRIPT.in4_6 
ROUTE SCRIPT.out4_6 TO FOU_SIX.diffuseColor   
 

##########################################
#------ MENU HIDING/SHOWING ROUTES ------#
##########################################

ROUTE T1.touchTime TO SCRIPT.click1 
ROUTE SCRIPT.whichChoice1 TO ONE.whichChoice 
ROUTE T2.touchTime TO SCRIPT.click2 
ROUTE SCRIPT.whichChoice2 TO TWO.whichChoice 
ROUTE T3.touchTime TO SCRIPT.click3 
ROUTE SCRIPT.whichChoice3 TO THR.whichChoice 
ROUTE T4.touchTime TO SCRIPT.click4 
ROUTE SCRIPT.whichChoice4 TO FOU.whichChoice 
ROUTE T5.touchTime TO SCRIPT.click5 
ROUTE SCRIPT.whichChoice5 TO FIV.whichChoice 
#ROUTE T6.touchTime TO SCRIPT.click6 
#ROUTE SCRIPT.whichChoice6 TO SIX.whichChoice 
#ROUTE T7.touchTime TO SCRIPT.click7 
#ROUTE SCRIPT.whichChoice7 TO SEV.whichChoice 
#ROUTE T8.touchTime TO SCRIPT.click8 
#ROUTE SCRIPT.whichChoice8 TO EIG.whichChoice
#ROUTE SCRIPT.whichChoice9 TO NIN.whichChoice 
ROUTE T1_1.touchTime TO SCRIPT.click1_1 
ROUTE SCRIPT.whichChoice1_1 TO ONE_ONE.whichChoice 
ROUTE T1_2.touchTime TO SCRIPT.click1_2 
ROUTE SCRIPT.whichChoice1_2 TO ONE_TWO.whichChoice 
ROUTE T1_3.touchTime TO SCRIPT.click1_3 
ROUTE SCRIPT.whichChoice1_3 TO ONE_THR.whichChoice 
ROUTE T1_4.touchTime TO SCRIPT.click1_4 
ROUTE SCRIPT.whichChoice1_4 TO ONE_FOU.whichChoice 
ROUTE T1_5.touchTime TO SCRIPT.click1_5 
ROUTE SCRIPT.whichChoice1_5 TO ONE_FIV.whichChoice 
ROUTE T1_6.touchTime TO SCRIPT.click1_6 
ROUTE SCRIPT.whichChoice1_6 TO ONE_SIX.whichChoice 
ROUTE T1_7.touchTime TO SCRIPT.click1_7 
ROUTE SCRIPT.whichChoice1_7 TO ONE_SEV.whichChoice 
ROUTE T1_8.touchTime TO SCRIPT.click1_8 
ROUTE SCRIPT.whichChoice1_8 TO ONE_EIG.whichChoice 
ROUTE T1_9.touchTime TO SCRIPT.click1_9 
ROUTE SCRIPT.whichChoice1_9 TO ONE_NIN.whichChoice 
ROUTE T1_10.touchTime TO SCRIPT.click1_10 
ROUTE SCRIPT.whichChoice1_10 TO ONE_TEN.whichChoice 
ROUTE T1_11.touchTime TO SCRIPT.click1_11 
ROUTE SCRIPT.whichChoice1_11 TO ONE_ELE.whichChoice 
ROUTE T1_12.touchTime TO SCRIPT.click1_12 
ROUTE SCRIPT.whichChoice1_12 TO ONE_TWE.whichChoice 
ROUTE T1_13.touchTime TO SCRIPT.click1_13 
ROUTE SCRIPT.whichChoice1_13 TO ONE_THI.whichChoice 
ROUTE T1_14.touchTime TO SCRIPT.click1_14 
ROUTE SCRIPT.whichChoice1_14 TO ONE_FOT.whichChoice 
ROUTE T1_15.touchTime TO SCRIPT.click1_15 
ROUTE SCRIPT.whichChoice1_15 TO ONE_FIT.whichChoice 
ROUTE T1_16.touchTime TO SCRIPT.click1_16 
ROUTE SCRIPT.whichChoice1_16 TO ONE_SIT.whichChoice 
ROUTE T1_17.touchTime TO SCRIPT.click1_17 
ROUTE SCRIPT.whichChoice1_17 TO ONE_SET.whichChoice 
ROUTE SCRIPT.whichChoice1_18 TO ONE_EIT.whichChoice 
ROUTE SCRIPT.whichChoice1_19 TO ONE_NIT.whichChoice 
ROUTE SCRIPT.whichChoice1_20 TO ONE_TTY.whichChoice 
ROUTE SCRIPT.whichChoice2_1 TO TWO_ONE.whichChoice  
ROUTE SCRIPT.whichChoice2_2 TO TWO_TWO.whichChoice 
ROUTE T2_3.touchTime TO SCRIPT.click2_3 
ROUTE SCRIPT.whichChoice2_3 TO TWO_THR.whichChoice
ROUTE SCRIPT.whichChoice2_4	TO TWO_FOU.whichChoice
ROUTE T3_1.touchTime TO SCRIPT.click3_1 
ROUTE SCRIPT.whichChoice3_1 TO THR_ONE.whichChoice
ROUTE T3_2.touchTime TO SCRIPT.click3_2 
ROUTE SCRIPT.whichChoice3_2 TO THR_TWO.whichChoice
ROUTE T3_3.touchTime TO SCRIPT.click3_3
ROUTE SCRIPT.whichChoice3_3 TO THR_THR.whichChoice
ROUTE T3_4.touchTime TO SCRIPT.click3_4 
ROUTE SCRIPT.whichChoice3_4 TO THR_FOU.whichChoice
ROUTE T3_5.touchTime TO SCRIPT.click3_5 
ROUTE SCRIPT.whichChoice3_5 TO THR_FIV.whichChoice
ROUTE T3_6.touchTime TO SCRIPT.click3_6 
ROUTE SCRIPT.whichChoice3_6 TO THR_SIX.whichChoice
ROUTE SCRIPT.whichChoice3_7 TO THR_SEV.whichChoice
ROUTE T4_1.touchTime TO SCRIPT.click4_1 
ROUTE SCRIPT.whichChoice4_1 TO FOU_ONE.whichChoice
ROUTE T4_2.touchTime TO SCRIPT.click4_2 
ROUTE SCRIPT.whichChoice4_2 TO FOU_TWO.whichChoice
ROUTE T4_3.touchTime TO SCRIPT.click4_3
ROUTE SCRIPT.whichChoice4_3 TO FOU_THR.whichChoice
ROUTE T4_4.touchTime TO SCRIPT.click4_4 
ROUTE SCRIPT.whichChoice4_4 TO FOU_FOU.whichChoice
ROUTE T4_5.touchTime TO SCRIPT.click4_5 
ROUTE SCRIPT.whichChoice4_5 TO FOU_FIV.whichChoice
ROUTE T4_6.touchTime TO SCRIPT.click4_6 
ROUTE SCRIPT.whichChoice4_6 TO FOU_SIX.whichChoice
ROUTE SCRIPT.whichChoice4_7 TO FOU_SEV.whichChoice

#######################################
#------ ROUTE FOR MOVING AVATAR ------#
#######################################
ROUTE MOVE_SENSOR.translation_changed TO AVATAR.translation

#####################################
#------ ROUTES FOR VIEWPOINTS ------#
#####################################
ROUTE T2_1.isActive TO SCRIPT.click2_1
ROUTE SCRIPT.output TO MAIN_VIEW.set_bind

ROUTE T2_2.isActive TO SCRIPT.click2_2
ROUTE SCRIPT.output2 TO FLOOR_VIEW.set_bind

##########################################
#------ ROUTES FOR CHANGING COLORS ------#
##########################################
ROUTE SCRIPT.skyColor TO BACK.skyColor
ROUTE SCRIPT.diffuseColor TO NIN.diffuseColor
ROUTE SCRIPT.diffuseColor TO ONE_EIT.diffuseColor
ROUTE SCRIPT.diffuseColor TO ONE_NIT.diffuseColor
ROUTE SCRIPT.diffuseColor TO ONE_TTY.diffuseColor
ROUTE SCRIPT.diffuseColor TO TWO_FOU.diffuseColor
ROUTE SCRIPT.diffuseColor TO THR_SEV.diffuseColor
ROUTE SCRIPT.diffuseColor TO FOU_SEV.diffuseColor


#######################################
#------ ROUTES FOR BOX PLATFORM ------#
#######################################
ROUTE SCRIPT.whichChoiceFLOOR TO FLOOR.whichChoice
ROUTE SCRIPT.whichChoiceRWALL TO RWALL.whichChoice
ROUTE SCRIPT.whichChoiceLWALL TO LWALL.whichChoice
ROUTE SCRIPT.whichChoiceBWALL TO BWALL.whichChoice
ROUTE SCRIPT.whichChoiceFWALL TO FWALL.whichChoice
ROUTE SCRIPT.whichChoiceROOF TO ROOF.whichChoice
ROUTE SCRIPT.translationFLOOR TO FLOOR.translation
ROUTE SCRIPT.translationRWALL TO RWALL.translation
ROUTE SCRIPT.translationLWALL TO LWALL.translation
ROUTE SCRIPT.translationBWALL TO BWALL.translation
ROUTE SCRIPT.translationFWALL TO FWALL.translation
ROUTE SCRIPT.translationROOF TO ROOF.translation

ROUTE SCRIPT.colorFLOOR	TO FLOOR.diffuseColor
ROUTE SCRIPT.colorRWALL	TO RWALL.diffuseColor
ROUTE SCRIPT.colorLWALL	TO LWALL.diffuseColor
ROUTE SCRIPT.colorBWALL	TO BWALL.diffuseColor
ROUTE SCRIPT.colorFWALL	TO FWALL.diffuseColor
ROUTE SCRIPT.colorROOF	TO ROOF.diffuseColor

ROUTE SCRIPT.position TO FLOOR_VIEW.position

