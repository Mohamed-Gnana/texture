from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import *
from math import *
import pygame
from pygame.tests.base_test import pygame

###variables ####
r=2
n=0
m=5
xcenterball=5
ycenterball=4
xcenter_pc=5.5
ycenter_pc=12
shiftx =.3
shifty=.3
pushed=False
quater4=False
quater3=False
quater2=False
quater1=False
side_right = False
side_left = False
side_top = False
side_bottom = False
shiftx_pc =.01
shifty_pc=0
quater_pc1=False
quater_pc2=False
quater_pc3=False
quater_pc4=False
pushed_pc=False
def hokey ():
    global n
    global m
    global r
    global xcenterball
    global ycenterball
    global xcenter_pc
    global ycenter_pc
    global shiftx
    global shifty
    global pushed
    global x1
    global x2
    global quater2
    global quater1
    global quater3
    global quater4
    global side_right
    global side_left
    global side_top
    global side_bottom
    global shiftx_pc
    global shifty_pc
    global quater_pc1
    global quater_pc2
    global quater_pc3
    global quater_pc4
    global pushed_pc



    distance = math.sqrt((m - xcenterball) *(m - xcenterball) + (n - ycenterball) * (n - ycenterball))
    distance_pc =math.sqrt((xcenter_pc-xcenterball)**2 +(ycenter_pc-ycenterball)**2)

    glClearColor(0,0,1,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0,0,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(0,0)
    glVertex2d(0,15)
    glVertex2d(10,15)
    glVertex2d(10,0)
    glEnd()
    glColor3f(1, 0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(.5, .5)
    glVertex2d(.5, 14.5)
    glVertex2d(9.5, 14.5)
    glVertex2d(9.5, .5)
    glEnd()
    glLineWidth(2)
    glColor3f(0, 0, 1, 0)
    glBegin(GL_LINES)
    glVertex2d(9.5, 7.5)
    glVertex2d(.5, 7.5)
    glEnd()


########center ##########
    radius = 1
    glColor3f(0, 1, 0, 1)
    glBegin(GL_POLYGON)
    for i in arange(0,2*pi,.001):
        cosine = radius * cos(i ) + 5
        sine = radius * sin(i ) + 7.5
        glVertex2f(cosine, sine)
    glEnd()
######ball#################
    glColor3f(0,0,0,0)
    glBegin(GL_POLYGON)
    for j in arange(0,2*pi,.001):
        xball=.5* cos (j)+xcenterball
        yball=.5*sin (j)+ycenterball
        glVertex2d(xball,yball)
    glEnd()


########goals #############
    glColor3f(1,1,1,1)
    glBegin(GL_POLYGON)
    for k in arange(0,2*pi,.001):
        xgoal1=1*sin(k)+5
        ygoal1=1*cos(k)
        glVertex2d(xgoal1,ygoal1)
    glEnd()

    glColor3f(1, 1, 1, 1)
    glBegin(GL_POLYGON)
    for q in arange(0,2*pi,.01):
        xgoal2=1*sin(q)+5
        ygoal2=1*cos(q)+15
        glVertex2d(xgoal2,ygoal2)
    glEnd()

#####first player ######
    glColor3f(0,2,1,4)
    glBegin(GL_POLYGON)
    for t in arange (0,2*pi,.01):
        xfirstplayer=.5*cos(t)+m
        yfirstplayer=.5*sin(t)+n
        glVertex2d(xfirstplayer,yfirstplayer)
    glEnd()
####pc_player  #####
    glColor3f(0,3,1,4)
    glBegin(GL_POLYGON)
    for num in arange (0,2*pi,.1):
        xsecondplayer=.5*cos(num)+xcenter_pc
        ysecondplayer=.5*sin(num)+ycenter_pc
        glVertex2d(xsecondplayer,ysecondplayer)
    glEnd()


########## movement for first player ####
    if n>7.5 :
        n=7.5
    if n<.5:
        n=.5
    if m<.5 :
        m=.5
    if m>9.5 :
        m=9.5

#############movementfor  pc #######
    ####the game low ######
    if ycenter_pc >= 14.5:
        ycenter_pc = 14.5
    if ycenter_pc <= 7.5:
        ycenter_pc = 7.5
    if xcenter_pc >= 9.5:
        xcenter_pc = 9.5
    if xcenter_pc <= .5:
        xcenter_pc = .5
    if ycenterball<=7.5 :
        xcenter_pc+=shiftx_pc
        if xcenter_pc>= 5.5 :
            xcenter_pc=5.5
            shiftx_pc =-.1
        if xcenter_pc<=4.5 :
            xcenter_pc =4.5
            shiftx_pc=.1

    if ycenterball>7.5 :
        xcenter_pc += shiftx_pc
        ycenter_pc += shifty_pc
        if distance_pc >= 1 and xcenter_pc != xcenterball:
            slope2= (ycenter_pc-ycenterball)/(xcenter_pc-xcenterball)
            if xcenterball>xcenter_pc and ycenterball > ycenter_pc:            ###الربع الاول #####
                quater_pc1=True
                quater_pc2=False
                quater_pc3=False
                quater_pc4=False
                shiftx_pc =.3
                #shifty_pc=(shiftx_pc)*slope2
            if xcenterball<xcenter_pc and ycenterball> ycenter_pc:      #الربع التاني ###
                quater_pc1=False
                quater_pc2=True
                quater_pc3=False
                quater_pc4=False
                shiftx_pc = -.3
                #shifty_pc=(shiftx_pc)*slope2

            if xcenterball<xcenter_pc and ycenterball<ycenter_pc:       ###الربع التالت
                quater_pc1=False
                quater_pc2=False
                quater_pc3=True
                quater_pc4=False
                shiftx_pc = -.3
                #shifty_pc = (shiftx_pc)*slope2

            if xcenterball>xcenter_pc and ycenterball<ycenter_pc:            ###الربع الرابع
                quater_pc1=False
                quater_pc2=False
                quater_pc3=False
                quater_pc4=True
                shiftx_pc = .3
               # shifty_pc = (shiftx_pc)*slope2

        if xcenterball > xcenter_pc and ycenterball==ycenter_pc:        ########الكره علي اليمين ######
            pushed_pc=True
            pushed = False
            shiftx_pc=.3
            shifty_pc=0
            if distance_pc<=1:
                shifty=0

        if xcenterball < xcenter_pc and ycenterball==ycenter_pc:        ########الكره علي الشمال  ######
            pushed_pc=True
            pushed = False
            shiftx_pc=-.3
            shifty_pc=0
            if distance_pc<= 1:
                shifty=0
        if xcenterball == xcenter_pc and ycenterball<=ycenter_pc:        ########الكره علي تحت ######
            pushed_pc=True
            pushed = False
            if xcenter_pc>7.5:
                shiftx_pc=0
            if distance_pc<=1:
                shiftx=0



        if distance_pc<= 1 :
            pushed_pc = True
            pushed =False




#### if goal  ########
    if xcenterball>=4.5 and xcenterball<=5.5  and ycenterball <= 1 :
        xcenterball=5
        ycenterball=7.5
        pushed=False
        pushed_pc=False


    if xcenterball>=4.5 and xcenterball<=5.5  and ycenterball >= 13.5 :
        xcenterball=5
        ycenterball=7.5
        pushed=False
        pushed_pc= False
        ####################the quater of the eqn ##########
    if xcenterball > m and ycenterball > n:    ####الربع الاول ######
        quater1 = True
        quater2 = False
        quater3 = False
        quater4 = False
        side_right = False
        side_left = False
        side_top = False
        side_bottom = False

    if xcenterball < m and ycenterball > n:   ####الربع التاني  ###
        quater1 = False
        quater2 = True
        quater3 = False
        quater4 = False
        side_right = False
        side_left = False
        side_top = False
        side_bottom = False

    if xcenterball < m and ycenterball < n:        ###الربع التالت  ##########
        quater1 = False
        quater2 = False
        quater3 = True
        quater4 = False
        side_right = False
        side_left = False
        side_top = False
        side_bottom = False
    if xcenterball > m and ycenterball < n:   ############### الربع الرابع  ###########
        quater1 = False
        quater2 = False
        quater3 = False
        quater4 = True
        side_right = False
        side_left = False
        side_top = False
        side_bottom = False

    if ycenterball == n and xcenterball >= m :    ########الكره يمين  ###########
        side_right = True
        side_left = False
        side_top = False
        side_bottom = False
        quater1 = False
        quater2 = False
        quater3 = False
        quater4 = False
    if ycenterball == n and xcenterball <= m :   #####الكره علي الشمال  #####
        side_right = False
        side_left = True
        side_top = False
        side_bottom = False
        quater1 = False
        quater2 = False
        quater3 = False
        quater4 = False


    if ycenterball >= n and xcenterball == m :    #####الكره فوووق  #######
        side_right = False
        side_left = False
        side_top = True
        side_bottom = False
        quater1 = False
        quater2 = False
        quater3 = False
        quater4 = False



    if ycenterball<= n and xcenterball == m :   #######الكره تحت  #######
        side_right = False
        side_left = False
        side_top = False
        side_bottom = True
        quater1 = False
        quater2 = False
        quater3 = False
        quater4 = False

        #######################################if they pushed #################
    if xcenterball != m  and distance<=1  :
        pushed=True
        pushed_pc=False
        slope = (ycenterball - n) / (xcenterball - m)
        if quater1 :
            shiftx =.3
            shifty = shiftx * slope
        elif quater2 :
            shiftx =-.3
            shifty = shiftx * slope
        elif quater3 :
            shiftx=-.3
            shifty = shiftx * slope
        elif quater4 :
            shiftx=.3
            shifty = shiftx * slope
    if  distance <= 1 :
        pushed = True
        pushed_pc =False
        if side_right:
            shiftx= .3
            shifty= 0

        elif side_left:
            shiftx=-shiftx
            shifty=0

        if side_top :
            shifty = .3
            shiftx =0

        elif side_bottom :
            shifty =-.3
            shiftx =0



######movement of ball ##########
    if xcenterball <=9.5 and xcenterball>=.5 and ycenterball >=.5 and ycenterball <=14.5 :
        if pushed ==True :
            xcenterball += shiftx
            ycenterball += shifty
        if pushed_pc ==True :
            xcenterball += shiftx
            ycenterball-= shifty
##############till the ball didn't get out match #######

    if xcenterball <=.5:
        xcenterball =.5
        shiftx=-shiftx

    if xcenterball >=9.5:
        xcenterball =9.5
        shiftx=-shiftx
    if ycenterball <=.5:
        ycenterball =.5
        shifty=-shifty

    if ycenterball >=14.5:
        ycenterball =14.5
        shifty=-shifty

    glFlush()
    glutPostRedisplay()
def keyboard (char , x,y):
    global m
    global n

    if char==GLUT_KEY_UP:
        n=n+.3
    if char==GLUT_KEY_DOWN:
        n=n-.3
    if char==GLUT_KEY_RIGHT:
        m=m+.3
    if char==GLUT_KEY_LEFT:
        m=m-.3
    glutPostRedisplay()
glutInit()

glutInitWindowSize(400,600)
glutCreateWindow(b'hokey')
glutInitWindowPosition(500,500)
gluOrtho2D(0,10,0,15)
glutSpecialFunc(keyboard)
#glutPassiveMotionFunc(mouse)
glutDisplayFunc(hokey)
glutIdleFunc(hokey)
glutMainLoop()
