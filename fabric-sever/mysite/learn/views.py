from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import asyncio
from hfc.fabric import Client
from hfc.protos.peer.proposal_response_pb2 import Response
import os
import json
import sys
sys.path.append("/home/fabric/crosschain/fabricabe/fabric-zdyf/ABE+")

from pol_trans import attr_pre
from django.shortcuts import render
import json

loop1 = asyncio.new_event_loop() 
asyncio.set_event_loop(loop1)
loop = asyncio.get_event_loop()


cli = Client(net_profile="/home/fabric/crosschain/fabricabe/fabric-zdyf/ABE+/testnetwork/network.json")

org2_admin = cli.get_user(org_name='org2.example.com', name='Admin')
org3_user = cli.get_user(org_name='org3.example.com', name='User1')
org3_admin = cli.get_user(org_name='org3.example.com', name='Admin')
org2_user = cli.get_user(org_name='org2.example.com', name='User1')
cli.new_channel('channel1')

find_reduestor = {
    
    'org2_admin':org2_admin,
    'org3_user':org3_user,
    'org3_admin':org3_admin,
    'org2_user':org2_user
}


def index(request):
    return HttpResponse("欢迎光临 自强学堂!")
# Create your views here.


def addCryptographAndPolicy(request):
    requestor_str = request.GET['requestor']
    requestor = find_reduestor[requestor_str]
    channel_name = request.GET['channel_name']
    peers = request.GET.getlist('peers')
    fcn = request.GET['fcn']
    policy_root = request.GET['policy_root']
    args = request.GET.getlist('args')
    args += attr_pre.bool_split(policy_root)
    cc_name = request.GET['cc_name']
    transient_map = None
    wait_for_event = True
    response = loop.run_until_complete(cli.chaincode_invoke(
               requestor = requestor,
               channel_name = channel_name,
               peers = peers,
               fcn = fcn,
               args = args,
               cc_name = cc_name,
               transient_map = transient_map, 
               wait_for_event= wait_for_event, 
               ))
    return HttpResponse(response)


def addUser(request):
    requestor_str = request.GET['requestor']
    requestor = find_reduestor[requestor_str]
    channel_name = request.GET['channel_name']
    peers = request.GET.getlist('peers')
    fcn = request.GET['fcn']
    # policy_root = request.GET['policy_root']
    args = request.GET.getlist('args')
    # args += attr_pre.bool_split(policy_root)
    cc_name = request.GET['cc_name']
    transient_map = None
    wait_for_event = True
    response = loop.run_until_complete(cli.chaincode_invoke(
               requestor = requestor,
               channel_name = channel_name,
               peers = peers,
               fcn = fcn,
               args = args,
               cc_name = cc_name,
               transient_map = transient_map, 
               wait_for_event= wait_for_event, 
               ))
    return HttpResponse(response)


def viewFilePermissions(request):
    requestor_str = request.GET['requestor']
    requestor = find_reduestor[requestor_str]
    channel_name = request.GET['channel_name']
    peers = request.GET.getlist('peers')
    fcn = request.GET['fcn']
    # policy_root = request.GET['policy_root']
    args = request.GET.getlist('args')
    # args += attr_pre.bool_split(policy_root)
    cc_name = request.GET['cc_name']
    transient_map = None
    wait_for_event = True
    response = loop.run_until_complete(cli.chaincode_invoke(
               requestor = requestor,
               channel_name = channel_name,
               peers = peers,
               fcn = fcn,
               args = args,
               cc_name = cc_name,
               transient_map = transient_map, 
               wait_for_event= wait_for_event, 
               ))
    return HttpResponse(response)

def askForPermissions(request):
    requestor_str = request.GET['requestor']
    requestor = find_reduestor[requestor_str]
    channel_name = request.GET['channel_name']
    peers = request.GET.getlist('peers')
    fcn = request.GET['fcn']
    # policy_root = request.GET['policy_root']
    args = request.GET.getlist('args')
    # args += attr_pre.bool_split(policy_root)
    cc_name = request.GET['cc_name']
    transient_map = None
    wait_for_event = True
    response = loop.run_until_complete(cli.chaincode_invoke(
               requestor = requestor,
               channel_name = channel_name,
               peers = peers,
               fcn = fcn,
               args = args,
               cc_name = cc_name,
               transient_map = transient_map, 
               wait_for_event= wait_for_event, 
               ))
    return HttpResponse(response)


def addCryptograph(request):
    requestor_str = request.GET['requestor']
    requestor = find_reduestor[requestor_str]
    channel_name = request.GET['channel_name']
    peers = request.GET.getlist('peers')
    fcn = request.GET['fcn']
    # policy_root = request.GET['policy_root']
    args = request.GET.getlist('args')
    # args += attr_pre.bool_split(policy_root)
    cc_name = request.GET['cc_name']
    transient_map = None
    wait_for_event = True
    response = loop.run_until_complete(cli.chaincode_invoke(
               requestor = requestor,
               channel_name = channel_name,
               peers = peers,
               fcn = fcn,
               args = args,
               cc_name = cc_name,
               transient_map = transient_map, 
               wait_for_event= wait_for_event, 
               ))
    return HttpResponse(response)


def addFileFlowInformation(request):
    requestor_str = request.GET['requestor']
    requestor = find_reduestor[requestor_str]
    channel_name = request.GET['channel_name']
    peers = request.GET.getlist('peers')
    fcn = request.GET['fcn']
    # policy_root = request.GET['policy_root']
    args = request.GET.getlist('args')
    # args += attr_pre.bool_split(policy_root)
    cc_name = request.GET['cc_name']
    transient_map = None
    wait_for_event = True
    response = loop.run_until_complete(cli.chaincode_invoke(
               requestor = requestor,
               channel_name = channel_name,
               peers = peers,
               fcn = fcn,
               args = args,
               cc_name = cc_name,
               transient_map = transient_map, 
               wait_for_event= wait_for_event, 
               ))
    return HttpResponse(response)


def viewAllDecryptionOperationNumbersOfTheFile(request):
    requestor_str = request.GET['requestor']
    requestor = find_reduestor[requestor_str]
    channel_name = request.GET['channel_name']
    peers = request.GET.getlist('peers')
    fcn = request.GET['fcn']
    # policy_root = request.GET['policy_root']
    args = request.GET.getlist('args')
    # args += attr_pre.bool_split(policy_root)
    cc_name = request.GET['cc_name']
    transient_map = None
    wait_for_event = True
    response = loop.run_until_complete(cli.chaincode_invoke(
               requestor = requestor,
               channel_name = channel_name,
               peers = peers,
               fcn = fcn,
               args = args,
               cc_name = cc_name,
               transient_map = transient_map, 
               wait_for_event= wait_for_event, 
               ))
    return HttpResponse(response)

