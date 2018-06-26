# -*- coding: utf-8 -*-
'''
Created on 21 de jun de 2018

@author: gcruzm
'''
from time import sleep

from selenium import webdriver
import pyautogui 


@given("Abrir tela do navegador")
def entrarNaTelaPrincipal(context):
    context.web = webdriver.Chrome()
    context.web.get("https://www.facebook.com.br")
    
@when("Logar no facebook")
def logarNoFacebook(context):
    context.web.maximize_window()

    #login
    email = context.web.find_element_by_id("email")
    email.send_keys("")
    sleep(2)
    
    #senha
    senha = context.web.find_element_by_id("pass")
    senha.send_keys("")
    sleep(5)
    
    #botao
    context.entrar = context.web.find_element_by_id("u_0_2").click()
    sleep(5)

@then("Escrever publicacao")  
def escreverPub(context):
    
    #caixa de pub
    publicar = context.web.find_element_by_name("xhpc_message")
    publicar.send_keys("aaaa")
    sleep(5)
    
    #bpub
    pub = context.web.find_element_by_class_name("_45wg _69yt")
    sleep(5)
    
    #edit
    edit = context.web.find_element_by_id("u_bu_c")
    e_pub = context.web.find_element_by_link_text("Editar publicação")
    publicar = context.web.find_element_by_name("xhpc_message")
    publicar.send_keys("aabbbb")
    button = context.web.find_element_by_class_name("_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft")    
    
