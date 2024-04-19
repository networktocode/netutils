"""Configuration conversion methods for different network operating systems."""

import re
import typing as t

from netutils.config.utils import _open_file_config

conversion_map: t.Dict[str, t.List[str]] = {
    "paloalto_panos": ["paloalto_panos_brace_to_set"],
}


def paloalto_panos_clean_newlines(cfg: str) -> str:
    r"""Takes in the configuration and replaces any inappropriate newline characters with a space.

    Args:
        cfg: Configuration as a string.

    Returns:
        str: Cleaned configuration as a string

    Examples:
        >>> from netutils.config.conversion import paloalto_panos_clean_newlines
        >>> config = '''
        ... config {
        ...     syslog {
        ...         Traffic_Syslog {
        ...             server {
        ...             splunk {
        ...                 transport UDP;
        ...                 port 514;
        ...                 format BSD;
        ...                 server 1.1.1.1;
        ...                 facility LOG_USER;
        ...             }
        ...             graylog {
        ...                 transport UDP;
        ...                 port 514;
        ...                 format BSD;
        ...                 server 2.2.2.2;
        ...                 facility LOG_USER;
        ...             }
        ...             }
        ...             format {
        ...             config "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$result|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial shost=$host cs3Label=Virtual System cs3=$vsys act=$cmd duser=$admin destinationServiceName=$client msg=$path externalId=$seqno PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSActionFlags=$actionflags
        ... Optional: cs1Label=Before Change Detail cs1=$before-change-detail cs2Label=After Change Detail cs2=$after-change-detail";
        ...             system "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial cs3Label=Virtual System cs3=$vsys fname=$object flexString2Label=Module flexString2=$module msg=$opaque externalId=$seqno cat=$eventid PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSActionFlags=$actionflags";
        ...             threat "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action request=$misc cs2Label=URL Category cs2=$category flexString2Label=Direction flexString2=$direction PanOSActionFlags=$actionflags externalId=$seqno cat=$threatid fileId=$pcap_id PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel PanOSThreatCategory=$thr_category PanOSContentVer=$contentver";
        ...             traffic "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action flexNumber1Label=Total bytes flexNumber1=$bytes in=$bytes_sent out=$bytes_received cn2Label=Packets cn2=$packets PanOSPacketsReceived=$pkts_received PanOSPacketsSent=$pkts_sent start=$cef-formatted-time_generated cn3Label=Elapsed time in seconds cn3=$elapsed cs2Label=URL Category cs2=$category externalId=$seqno reason=$session_end_reason PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name cat=$action_source PanOSActionFlags=$actionflags PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel";
        ...             url "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action request=$misc cs2Label=URL Category cs2=$category flexString2Label=Direction flexString2=$direction PanOSActionFlags=$actionflags externalId=$seqno requestContext=$contenttype cat=$threatid fileId=$pcap_id requestMethod=$http_method requestClientApplication=$user_agent PanOSXForwarderfor=$xff PanOSReferer=$referer PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel PanOSThreatCategory=$thr_category PanOSContentVer=$contentver";
        ...             data "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action request=$misc cs2Label=URL Category cs2=$category flexString2Label=Direction flexString2=$direction PanOSActionFlags=$actionflags externalId=$seqno cat=$threatid fileId=$pcap_id PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel PanOSThreatCategory=$thr_category PanOSContentVer=$contentver";
        ...             wildfire "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action request=$misc cs2Label=URL Category cs2=$category flexString2Label=Direction flexString2=$direction PanOSActionFlags=$actionflags externalId=$seqno cat=$threatid filePath=$cloud fileId=$pcap_id fileHash=$filedigest fileType=$filetype suid=$sender msg=$subject duid=$recipient oldFileId=$reportid PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel PanOSThreatCategory=$thr_category PanOSContentVer=$contentver";
        ...             tunnel "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=Log Action cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action externalId=$seqno PanOSActionFlags=$actionflags PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time cs2Label=Tunnel Type cs2=$tunnel flexNumber1Label=Total bytes flexNumber1=$bytes in=$bytes_sent out=$bytes_received cn2Label=Packets cn2=$packets PanOSPacketsSent=$pkts_sent PanOSPacketsReceived=$pkts_received flexNumber2Label=Maximum Encapsulation flexNumber2=$max_encap cfp1Label=Unknown Protocol cfp1=$unknown_proto cfp2Label=Strict Checking cfp2=$strict_check PanOSTunnelFragment=$tunnel_fragment cfp3Label=Sessions Created cfp3=$sessions_created cfp4Label=Sessions Closed cfp4=$sessions_closed reason=$session_end_reason cat=$action_source start=$cef-formatted-time_generated cn3Label=Elapsed time in seconds cn3=$elapsed";
        ...             auth "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial cs1Label=Server Profile cs1=$serverprofile cs2Label=Normalize User cs2=$normalize_user cs3Label=Virtual System cs3=$vsys cs4Label=Authentication Policy cs4=$authpolicy cs5Label=Client Type cs5=$clienttype cs6Label=Log Action cs6=$logset fname=$object cn1Label=Factor Number cn1=$factorno cn2Label=Authentication ID cn2=$authid src=$ip cnt=$repeatcnt duser=$user flexString2Label=Vendor flexString2=$vendor msg=$event externalId=$seqno PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSActionFlags=$actionflags PanOSDesc=$desc
        ... ";
        ...             userid "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial cs1Label=Factor Type cs1=$factortype cs3Label=Virtual System cs3=$vsys cs4Label=Data Source Name cs4=$datasourcename cs5Label=Data Source cs5=$datasource cs6Label=Data Source Type cs6=$datasourcetype cn1Label=Factor Number cn1=$factorno cn2Label=Virtual System ID cn2=$vsys_id cn3Label=Timeout Threshold cn3=$timeout src=$ip spt=$beginport dpt=$endport cnt=$repeatcnt duser=$user externalId=$seqno cat=$eventid end=$factorcompletiontime PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSActionFlags=$actionflags";
        ...             hip-match "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$matchtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial suser=$srcuser cs3Label=Virtual System cs3=$vsys shost=$machinename src=$src cnt=$repeatcnt externalId=$seqno cat=$matchname start=$cef-formatted-time_generated cs2Label=Operating System cs2=$os PanOSActionFlags=$actionflags PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name cn2Label=Virtual System ID cn2=$vsys_id c6a2Label=IPv6 Source Address c6a2=$srcipv6";
        ...             correlation "CEF:0|Palo Alto Networks|PAN-OS|8.0|$category|$type|$severity|rt=$cef-formatted-receive_time deviceExternalId=$serial start=$cef-formatted-time_generated src=$src suser=$srcuser cs3Label=Virtual System cs3=$vsys severity=$severity PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name cn2Label=Virtual System ID cn2=$vsys_id fname=$object_name cn3Label=Object ID cn3=$object_id msg=$evidence";
        ...             escaping {
        ...                 escaped-characters \=;
        ...                 escape-character \;
        ...             }
        ...             }
        ...         }
        ...         }
        ... }'''
        >>> paloalto_panos_clean_newlines(cfg=config) == \
        ... '''
        ... config {
        ...     syslog {
        ...         Traffic_Syslog {
        ...             server {
        ...             splunk {
        ...                 transport UDP;
        ...                 port 514;
        ...                 format BSD;
        ...                 server 1.1.1.1;
        ...                 facility LOG_USER;
        ...             }
        ...             graylog {
        ...                 transport UDP;
        ...                 port 514;
        ...                 format BSD;
        ...                 server 2.2.2.2;
        ...                 facility LOG_USER;
        ...             }
        ...             }
        ...             format {
        ...             config "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$result|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial shost=$host cs3Label=Virtual System cs3=$vsys act=$cmd duser=$admin destinationServiceName=$client msg=$path externalId=$seqno PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSActionFlags=$actionflags Optional: cs1Label=Before Change Detail cs1=$before-change-detail cs2Label=After Change Detail cs2=$after-change-detail";
        ...             system "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial cs3Label=Virtual System cs3=$vsys fname=$object flexString2Label=Module flexString2=$module msg=$opaque externalId=$seqno cat=$eventid PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSActionFlags=$actionflags";
        ...             threat "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action request=$misc cs2Label=URL Category cs2=$category flexString2Label=Direction flexString2=$direction PanOSActionFlags=$actionflags externalId=$seqno cat=$threatid fileId=$pcap_id PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel PanOSThreatCategory=$thr_category PanOSContentVer=$contentver";
        ...             traffic "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action flexNumber1Label=Total bytes flexNumber1=$bytes in=$bytes_sent out=$bytes_received cn2Label=Packets cn2=$packets PanOSPacketsReceived=$pkts_received PanOSPacketsSent=$pkts_sent start=$cef-formatted-time_generated cn3Label=Elapsed time in seconds cn3=$elapsed cs2Label=URL Category cs2=$category externalId=$seqno reason=$session_end_reason PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name cat=$action_source PanOSActionFlags=$actionflags PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel";
        ...             url "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action request=$misc cs2Label=URL Category cs2=$category flexString2Label=Direction flexString2=$direction PanOSActionFlags=$actionflags externalId=$seqno requestContext=$contenttype cat=$threatid fileId=$pcap_id requestMethod=$http_method requestClientApplication=$user_agent PanOSXForwarderfor=$xff PanOSReferer=$referer PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel PanOSThreatCategory=$thr_category PanOSContentVer=$contentver";
        ...             data "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action request=$misc cs2Label=URL Category cs2=$category flexString2Label=Direction flexString2=$direction PanOSActionFlags=$actionflags externalId=$seqno cat=$threatid fileId=$pcap_id PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel PanOSThreatCategory=$thr_category PanOSContentVer=$contentver";
        ...             wildfire "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|$number-of-severity|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=LogProfile cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action request=$misc cs2Label=URL Category cs2=$category flexString2Label=Direction flexString2=$direction PanOSActionFlags=$actionflags externalId=$seqno cat=$threatid filePath=$cloud fileId=$pcap_id fileHash=$filedigest fileType=$filetype suid=$sender msg=$subject duid=$recipient oldFileId=$reportid PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSSrcUUID=$src_uuid PanOSDstUUID=$dst_uuid PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time PanOSTunnelType=$tunnel PanOSThreatCategory=$thr_category PanOSContentVer=$contentver";
        ...             tunnel "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial src=$src dst=$dst sourceTranslatedAddress=$natsrc destinationTranslatedAddress=$natdst cs1Label=Rule cs1=$rule suser=$srcuser duser=$dstuser app=$app cs3Label=Virtual System cs3=$vsys cs4Label=Source Zone cs4=$from cs5Label=Destination Zone cs5=$to deviceInboundInterface=$inbound_if deviceOutboundInterface=$outbound_if cs6Label=Log Action cs6=$logset cn1Label=SessionID cn1=$sessionid cnt=$repeatcnt spt=$sport dpt=$dport sourceTranslatedPort=$natsport destinationTranslatedPort=$natdport flexString1Label=Flags flexString1=$flags proto=$proto act=$action externalId=$seqno PanOSActionFlags=$actionflags PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSTunnelID=$tunnelid PanOSMonitorTag=$monitortag PanOSParentSessionID=$parent_session_id PanOSParentStartTime=$parent_start_time cs2Label=Tunnel Type cs2=$tunnel flexNumber1Label=Total bytes flexNumber1=$bytes in=$bytes_sent out=$bytes_received cn2Label=Packets cn2=$packets PanOSPacketsSent=$pkts_sent PanOSPacketsReceived=$pkts_received flexNumber2Label=Maximum Encapsulation flexNumber2=$max_encap cfp1Label=Unknown Protocol cfp1=$unknown_proto cfp2Label=Strict Checking cfp2=$strict_check PanOSTunnelFragment=$tunnel_fragment cfp3Label=Sessions Created cfp3=$sessions_created cfp4Label=Sessions Closed cfp4=$sessions_closed reason=$session_end_reason cat=$action_source start=$cef-formatted-time_generated cn3Label=Elapsed time in seconds cn3=$elapsed";
        ...             auth "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial cs1Label=Server Profile cs1=$serverprofile cs2Label=Normalize User cs2=$normalize_user cs3Label=Virtual System cs3=$vsys cs4Label=Authentication Policy cs4=$authpolicy cs5Label=Client Type cs5=$clienttype cs6Label=Log Action cs6=$logset fname=$object cn1Label=Factor Number cn1=$factorno cn2Label=Authentication ID cn2=$authid src=$ip cnt=$repeatcnt duser=$user flexString2Label=Vendor flexString2=$vendor msg=$event externalId=$seqno PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSActionFlags=$actionflags PanOSDesc=$desc ";
        ...             userid "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$subtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial cs1Label=Factor Type cs1=$factortype cs3Label=Virtual System cs3=$vsys cs4Label=Data Source Name cs4=$datasourcename cs5Label=Data Source cs5=$datasource cs6Label=Data Source Type cs6=$datasourcetype cn1Label=Factor Number cn1=$factorno cn2Label=Virtual System ID cn2=$vsys_id cn3Label=Timeout Threshold cn3=$timeout src=$ip spt=$beginport dpt=$endport cnt=$repeatcnt duser=$user externalId=$seqno cat=$eventid end=$factorcompletiontime PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name PanOSActionFlags=$actionflags";
        ...             hip-match "CEF:0|Palo Alto Networks|PAN-OS|$sender_sw_version|$matchtype|$type|1|rt=$cef-formatted-receive_time deviceExternalId=$serial suser=$srcuser cs3Label=Virtual System cs3=$vsys shost=$machinename src=$src cnt=$repeatcnt externalId=$seqno cat=$matchname start=$cef-formatted-time_generated cs2Label=Operating System cs2=$os PanOSActionFlags=$actionflags PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name cn2Label=Virtual System ID cn2=$vsys_id c6a2Label=IPv6 Source Address c6a2=$srcipv6";
        ...             correlation "CEF:0|Palo Alto Networks|PAN-OS|8.0|$category|$type|$severity|rt=$cef-formatted-receive_time deviceExternalId=$serial start=$cef-formatted-time_generated src=$src suser=$srcuser cs3Label=Virtual System cs3=$vsys severity=$severity PanOSDGl1=$dg_hier_level_1 PanOSDGl2=$dg_hier_level_2 PanOSDGl3=$dg_hier_level_3 PanOSDGl4=$dg_hier_level_4 PanOSVsysName=$vsys_name dvchost=$device_name cn2Label=Virtual System ID cn2=$vsys_id fname=$object_name cn3Label=Object ID cn3=$object_id msg=$evidence";
        ...             escaping {
        ...                 escaped-characters \=;
        ...                 escape-character \;
        ...             }
        ...             }
        ...         }
        ...         }
        ... }'''
        True
    """
    paloalto_panos_no_newline_cleanup_match = ["private-key", "public-key", "login-banner"]
    paloalto_panos_newline_regex = re.compile(
        r"\w+?-?\w+\s\"(?:[^\"\\]|\\.)*\n(?:[^\"\\]|\\.)*\";$", re.MULTILINE | re.DOTALL
    )

    newlines_cleaned_cfg = paloalto_panos_newline_regex.sub(
        lambda match: (
            match.group().replace("\n", " ")
            if not any(substring in match.group() for substring in paloalto_panos_no_newline_cleanup_match)
            else match.group()
        ),
        cfg,
    )

    return newlines_cleaned_cfg


def paloalto_panos_brace_to_set(cfg: str, cfg_type: str = "file") -> str:
    r"""Convert Palo Alto Brace format configuration to set format.

    Args:
        cfg: Configuration as a string
        cfg_type: A string that is effectively a choice between `file` and `string`. Defaults to `file`.

    Returns:
        str: Converted configuration as a string.

    Examples:
        >>> from netutils.config.conversion import paloalto_panos_brace_to_set
        >>> config = '''
        ...     config {
        ...            mgt-config {
        ...                users {
        ...                  admin {
        ...                    phash *;
        ...                    permissions {
        ...                      role-based {
        ...                        superuser yes;
        ...                      }
        ...                    }
        ...                    public-key thisisasuperduperlongbase64encodedstring;
        ...                }
        ...                panadmin {
        ...                    permissions {
        ...                      role-based {
        ...                        superuser yes;
        ...                      }
        ...                    }
        ...                    phash passwordhash;
        ...                }
        ...              }
        ...            }
        ...         }'''
        >>> paloalto_panos_brace_to_set(cfg=config, cfg_type='string') == \
        ... '''set mgt-config users admin phash *
        ... set mgt-config users admin permissions role-based superuser yes
        ... set mgt-config users admin public-key thisisasuperduperlongbase64encodedstring
        ... set mgt-config users panadmin permissions role-based superuser yes
        ... set mgt-config users panadmin phash passwordhash'''
        True
    """
    stack: t.List[str] = []
    cfg_value: t.List[str] = []
    cfg_string: str = ""

    if cfg_type not in ["file", "string"]:
        raise ValueError("The variable `cfg_type` must be either `file` or `string`.")
    if cfg_type == "file":
        cfg_raw = _open_file_config(cfg)
        cfg_list = paloalto_panos_clean_newlines(cfg=cfg_raw).splitlines()
    else:
        cfg_raw = paloalto_panos_clean_newlines(cfg=cfg)
        cfg_list = cfg_raw.splitlines()

    for i, line in enumerate(cfg_list):
        line = line.strip()
        if line.endswith(";") and not line.startswith('";'):
            line = line.split(";", 1)[0]
            line = "".join(str(s) for s in stack) + line
            line = line.split("config ", 1)[1]
            line = "set " + line
            cfg_value.append(line.strip())
        elif line.endswith('login-banner "') or line.endswith('content "'):
            _first_banner_line = "".join(str(s) for s in stack) + line
            cfg_value.append("set " + _first_banner_line.split("config ", 1)[1])

            for banner_line in cfg_list[i + 1:]:  # fmt: skip
                if '"' in banner_line:
                    banner_line = banner_line.split(";", 1)[0]
                    cfg_value.append(banner_line.strip())
                    break
                cfg_value.append(banner_line.strip())
        elif line.endswith("{"):
            stack.append(line[:-1])
        elif line == "}" and len(stack) > 0:
            stack.pop()

    for _l, _line in enumerate(cfg_value):
        cfg_string += _line
        if _l < len(cfg_value) - 1:
            cfg_string += "\n"

    # Filter out 'devices localhost.local domain' from the entire cfg_string
    # TODO: Add flagging capability to disable this behavior
    cfg_string = cfg_string.replace("devices localhost.localdomain ", "")

    return cfg_string
