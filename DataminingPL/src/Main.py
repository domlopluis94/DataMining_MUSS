import json
import csv
import pandas as pd

# season 1

from pprint import pprint


class Player:
    name: ''
    position: ''
    rate: ''
    blocks: ''
    passAccurate: ''
    totalPass: ''
    touches: ''
    fouls: ''
    tackles: ''
    lost: ''
    goals: ''
    won_contest: ''
    yellow_card:''
    red_card:''
    assistence:''


def mainClass():
    # '../datafile/season14-15/season_match_stats.json'

    vard = {}
    vart = json.dumps(vard)

    def main():
        ficheros = ["../datafile/season14-15/","../datafile/season15-16/","../datafile/season16-17/",
                    "../datafile/season17-18/"]
        # jsontocsv("validfinal.json")
        seasonid =0
        for dirname in ficheros:
            seasonid = Playerdatset(dirname, seasonid)
            #   seasonid = parseojson(dirname,seasonid)

    def parseojson(season,seasonid):
        global_idpartidos = seasonid

        dirm = season+"season_match_stats.json"
        dirs = season+"season_stats.json"
        with open(dirm) as match:
            datamat = json.load(match)
        with open(dirs) as matchstat:
            datastats = json.load(matchstat)
        # la idea primera es añadir a matach cada extrastats
        idt = ["",""]
        for id in datamat:
                punt = 0
                for idtema in datastats[id]:
                    idt[punt] = idtema
                    punt = punt+1
                dataone = ajustdata(datastats,idt[0],id)
                datatwo = ajustdata(datastats, idt[1], id)
                final = result(datamat[id]['full_time_score'])
                matcjob = {
                    global_idpartidos: {
                        "season": season[-6:-1],
                        "home_team_id": datamat[id]['home_team_id'],
                        "away_team_id": datamat[id]['away_team_id'],
                        "home_team_name": datamat[id]['home_team_name'],
                        "away_team_name": datamat[id]['away_team_name'],
                        "date_string": datamat[id]['date_string'],
                        "half_time_score": datamat[id]['half_time_score'],
                        "full_time_score": datamat[id]['full_time_score'],
                        "full_time_result": final,
                        "home_att_goal_low_left": dataone[0],
                        "home_won_contest": dataone[1],
                        "home_possession_percentage": dataone[2],
                        "home_total_throws": dataone[3],
                        "home_att_miss_high_left": dataone[4],
                        "home_blocked_scoring_att": dataone[5],
                        "home_total_scoring_att": dataone[6],
                        "home_att_sv_low_left": dataone[7],
                        "home_total_tackle": dataone[8],
                        "home_att_miss_high_right": dataone[9],
                        "home_aerial_won": dataone[10],
                        "home_att_miss_right": dataone[11],
                        "home_att_sv_low_centre":dataone[12],
                        "home_aerial_lost": dataone[13],
                        "home_accurate_pass": dataone[14],
                        "home_total_pass": dataone[15],
                        "home_won_corners": dataone[16],
                        "home_shot_off_target": dataone[17],
                        "home_ontarget_scoring_att": dataone[18],
                        "home_goals": dataone[19],
                        "home_att_miss_left": dataone[20],
                        "home_fk_foul_lost": dataone[21],
                        "home_att_sv_low_right": dataone[22],
                        "home_att_goal_low_centre": dataone[23],
                        "away_att_goal_low_left": datatwo[0],
                        "away_won_contest": datatwo[1],
                        "away_possession_percentage": datatwo[2],
                        "away_total_throws": datatwo[3],
                        "away_att_miss_high_left": datatwo[4],
                        "away_blocked_scoring_att": datatwo[5],
                        "away_total_scoring_att": datatwo[6],
                        "away_att_sv_low_left": datatwo[7],
                        "away_total_tackle": datatwo[8],
                        "away_att_miss_high_right": datatwo[9],
                        "away_aerial_won": datatwo[10],
                        "away_att_miss_right": datatwo[11],
                        "away_att_sv_low_centre": datatwo[12],
                        "away_aerial_lost": datatwo[13],
                        "away_accurate_pass": datatwo[14],
                        "away_total_pass": datatwo[15],
                        "away_won_corners": datatwo[16],
                        "away_shot_off_target": datatwo[17],
                        "away_ontarget_scoring_att": datatwo[18],
                        "away_goals": datatwo[19],
                        "away_att_miss_left": datatwo[20],
                        "away_fk_foul_lost": datatwo[21],
                        "away_att_sv_low_right": datatwo[22],
                        "away_att_goal_low_centre": datatwo[22]
                    }
                }
                global_idpartidos = global_idpartidos +1
                print(json.dumps(matcjob))

                with open('final.json') as f:
                    data = json.load(f)

                data.update(matcjob)

                with open('final.json', 'w') as f:
                    json.dump(data, f)
        return global_idpartidos



    def ajustdata(datastats,idt,id):
        # hay algunos que no tiene
        ret = ["","","","","","","","","","","","","","","","","","","","","","","",""]
        try:
            ret[0] = datastats[id][idt]['aggregate_stats']['att_goal_low_left']
        except:
            ret[0] = ""
        try:
            ret[1] = datastats[id][idt]['aggregate_stats']['won_contest']
        except:
            ret[1] = ""
        try:
            ret[2] = datastats[id][idt]['aggregate_stats']['possession_percentage']
        except:
            ret[2] = ""
        try:
            ret[3] = datastats[id][idt]['aggregate_stats']['total_throws']
        except:
            ret[3] = ""
        try:
            ret[4] = datastats[id][idt]['aggregate_stats']['att_miss_high_left']
        except:
            ret[4] = ""
        try:
            ret[5] = datastats[id][idt]['aggregate_stats']['blocked_scoring_att']
        except:
            ret[5] = ""
        try:
            ret[6] = datastats[id][idt]['aggregate_stats']['total_scoring_att']
        except:
            ret[6] = ""
        try:
            ret[7] = datastats[id][idt]['aggregate_stats']['att_sv_low_left']
        except:
            ret[7] = ""
        try:
            ret[8] = datastats[id][idt]['aggregate_stats']['total_tackle']
        except:
            ret[8] = ""
        try:
            ret[9] = datastats[id][idt]['aggregate_stats']['att_miss_high_right']
        except:
            ret[9] = ""
        try:
            ret[10] = datastats[id][idt]['aggregate_stats']['aerial_won']
        except:
            ret[10] = ""
        try:
            ret[11] = datastats[id][idt]['aggregate_stats']['att_miss_right']
        except:
            ret[11] = ""
        try:
            ret[12] = datastats[id][idt]['aggregate_stats']['att_sv_low_centre']
        except:
            ret[12] = ""
        try:
            ret[13] = datastats[id][idt]['aggregate_stats']['aerial_lost']
        except:
            ret[13] = ""
        try:
            ret[14] = datastats[id][idt]['aggregate_stats']['accurate_pass']
        except:
            ret[14] = ""
        try:
            ret[15] = datastats[id][idt]['aggregate_stats']['total_pass']
        except:
            ret[15] = ""
        try:
            ret[16] = datastats[id][idt]['aggregate_stats']['won_corners']
        except:
            ret[16] = ""
        try:
            ret[17] = datastats[id][idt]['aggregate_stats']['shot_off_target']
        except:
            ret[17] = ""
        try:
            ret[18] = datastats[id][idt]['aggregate_stats']['ontarget_scoring_att']
        except:
            ret[18] = ""
        try:
            ret[19] = datastats[id][idt]['aggregate_stats']['goals']
        except:
            ret[19] = ""
        try:
            ret[20] = datastats[id][idt]['aggregate_stats']['att_miss_left']
        except:
            ret[20] = ""
        try:
            ret[21] = datastats[id][idt]['aggregate_stats']['fk_foul_lost']
        except:
            ret[21] = ""
        try:
            ret[22] = datastats[id][idt]['aggregate_stats']['att_sv_low_right']
        except:
            ret[22] = ""
        try:
            ret[23] = datastats[id][idt]['aggregate_stats']['att_goal_low_centre']
        except:
            ret[23] = ""
        return ret

    def result(data):
        home = data[0]
        away = data[-1]
        if home > away:
            return "H"
        elif home < away:
            return "A"
        else:
            return "D"

    def Playerdatset(season,seasonid):
        global_idpartidos = seasonid

        dirm = season + "season_match_stats.json"
        dirs = season + "season_stats.json"
        with open(dirm) as match:
            datamat = json.load(match)
        with open(dirs) as matchstat:
            datastats = json.load(matchstat)
        # la idea primera es añadir a matach cada extrastats
        idt = ["", ""]
        for id in datamat:
            punt = 0
            for idtema in datastats[id]:
                idt[punt] = idtema
                punt = punt + 1
            # vamos a ajustar los datos de cada jugador para cada partido

            homeTeam = teamPlayerArray(datastats, idt[0], id)
            visitTeam = teamPlayerArray(datastats, idt[0], id)
            final = result(datamat[id]['full_time_score'])
            matcjob = {
                global_idpartidos: {
                    "season": season[-6:-1],
                    "home_team_name": datamat[id]['home_team_name'],
                    "away_team_name": datamat[id]['away_team_name'],
                    "half_time_score": datamat[id]['half_time_score'],
                    "full_time_score": datamat[id]['full_time_score'],
                    "full_time_result": final,
                    "home_" + homeTeam[0].position + "_name": homeTeam[0].name,
                    "home_" + homeTeam[0].position + "_assistence": homeTeam[0].assistence,
                    "home_" + homeTeam[0].position + "_won_contest": homeTeam[0].won_contest,
                    "home_" + homeTeam[0].position + "_tackles": homeTeam[0].tackles,
                    "home_" + homeTeam[0].position + "_goals": homeTeam[0].goals,
                    "home_" + homeTeam[0].position + "_red_card": homeTeam[0].red_card,
                    "home_" + homeTeam[0].position + "_yellow_card": homeTeam[0].yellow_card,
                    "home_" + homeTeam[0].position + "_touches": homeTeam[0].touches,
                    "home_" + homeTeam[0].position + "_lost": homeTeam[0].lost,
                    "home_" + homeTeam[0].position + "_rate": homeTeam[0].rate,
                    "home_" + homeTeam[0].position + "_fouls": homeTeam[0].fouls,
                    "home_" + homeTeam[0].position + "_blocks": homeTeam[0].blocks,
                    "home_" + homeTeam[1].position + "_name": homeTeam[1].name,
                    "home_" + homeTeam[1].position + "_assistence": homeTeam[1].assistence,
                    "home_" + homeTeam[1].position + "_won_contest": homeTeam[1].won_contest,
                    "home_" + homeTeam[1].position + "_tackles": homeTeam[1].tackles,
                    "home_" + homeTeam[1].position + "_goals": homeTeam[1].goals,
                    "home_" + homeTeam[1].position + "_red_card": homeTeam[1].red_card,
                    "home_" + homeTeam[1].position + "_yellow_card": homeTeam[1].yellow_card,
                    "home_" + homeTeam[1].position + "_touches": homeTeam[1].touches,
                    "home_" + homeTeam[1].position + "_lost": homeTeam[1].lost,
                    "home_" + homeTeam[1].position + "_rate": homeTeam[1].rate,
                    "home_" + homeTeam[1].position + "_fouls": homeTeam[1].fouls,
                    "home_" + homeTeam[1].position + "_blocks": homeTeam[1].blocks,
                    "home_" + homeTeam[2].position + "_name": homeTeam[2].name,
                    "home_" + homeTeam[2].position + "_assistence": homeTeam[2].assistence,
                    "home_" + homeTeam[2].position + "_won_contest": homeTeam[2].won_contest,
                    "home_" + homeTeam[2].position + "_tackles": homeTeam[2].tackles,
                    "home_" + homeTeam[2].position + "_goals": homeTeam[2].goals,
                    "home_" + homeTeam[2].position + "_red_card": homeTeam[2].red_card,
                    "home_" + homeTeam[2].position + "_yellow_card": homeTeam[2].yellow_card,
                    "home_" + homeTeam[2].position + "_touches": homeTeam[2].touches,
                    "home_" + homeTeam[2].position + "_lost": homeTeam[2].lost,
                    "home_" + homeTeam[2].position + "_rate": homeTeam[2].rate,
                    "home_" + homeTeam[2].position + "_fouls": homeTeam[2].fouls,
                    "home_" + homeTeam[2].position + "_blocks": homeTeam[2].blocks,
                    "home_" + homeTeam[3].position + "_name": homeTeam[3].name,
                    "home_" + homeTeam[3].position + "_assistence": homeTeam[3].assistence,
                    "home_" + homeTeam[3].position + "_won_contest": homeTeam[3].won_contest,
                    "home_" + homeTeam[3].position + "_tackles": homeTeam[3].tackles,
                    "home_" + homeTeam[3].position + "_goals": homeTeam[3].goals,
                    "home_" + homeTeam[3].position + "_red_card": homeTeam[3].red_card,
                    "home_" + homeTeam[3].position + "_yellow_card": homeTeam[3].yellow_card,
                    "home_" + homeTeam[3].position + "_touches": homeTeam[3].touches,
                    "home_" + homeTeam[3].position + "_lost": homeTeam[3].lost,
                    "home_" + homeTeam[3].position + "_rate": homeTeam[3].rate,
                    "home_" + homeTeam[3].position + "_fouls": homeTeam[3].fouls,
                    "home_" + homeTeam[3].position + "_blocks": homeTeam[3].blocks,
                    "home_" + homeTeam[4].position + "_name": homeTeam[4].name,
                    "home_" + homeTeam[4].position + "_assistence": homeTeam[4].assistence,
                    "home_" + homeTeam[4].position + "_won_contest": homeTeam[4].won_contest,
                    "home_" + homeTeam[4].position + "_tackles": homeTeam[4].tackles,
                    "home_" + homeTeam[4].position + "_goals": homeTeam[4].goals,
                    "home_" + homeTeam[4].position + "_red_card": homeTeam[4].red_card,
                    "home_" + homeTeam[4].position + "_yellow_card": homeTeam[4].yellow_card,
                    "home_" + homeTeam[4].position + "_touches": homeTeam[4].touches,
                    "home_" + homeTeam[4].position + "_lost": homeTeam[4].lost,
                    "home_" + homeTeam[4].position + "_rate": homeTeam[4].rate,
                    "home_" + homeTeam[4].position + "_fouls": homeTeam[4].fouls,
                    "home_" + homeTeam[4].position + "_blocks": homeTeam[4].blocks,
                    "home_" + homeTeam[5].position + "_name": homeTeam[5].name,
                    "home_" + homeTeam[5].position + "_assistence": homeTeam[5].assistence,
                    "home_" + homeTeam[5].position + "_won_contest": homeTeam[5].won_contest,
                    "home_" + homeTeam[5].position + "_tackles": homeTeam[5].tackles,
                    "home_" + homeTeam[5].position + "_goals": homeTeam[5].goals,
                    "home_" + homeTeam[5].position + "_red_card": homeTeam[5].red_card,
                    "home_" + homeTeam[5].position + "_yellow_card": homeTeam[5].yellow_card,
                    "home_" + homeTeam[5].position + "_touches": homeTeam[5].touches,
                    "home_" + homeTeam[5].position + "_lost": homeTeam[5].lost,
                    "home_" + homeTeam[5].position + "_rate": homeTeam[5].rate,
                    "home_" + homeTeam[5].position + "_fouls": homeTeam[5].fouls,
                    "home_" + homeTeam[5].position + "_blocks": homeTeam[5].blocks,
                    "home_" + homeTeam[6].position + "_name": homeTeam[6].name,
                    "home_" + homeTeam[6].position + "_assistence": homeTeam[6].assistence,
                    "home_" + homeTeam[6].position + "_won_contest": homeTeam[6].won_contest,
                    "home_" + homeTeam[6].position + "_tackles": homeTeam[6].tackles,
                    "home_" + homeTeam[6].position + "_goals": homeTeam[6].goals,
                    "home_" + homeTeam[6].position + "_red_card": homeTeam[6].red_card,
                    "home_" + homeTeam[6].position + "_yellow_card": homeTeam[6].yellow_card,
                    "home_" + homeTeam[6].position + "_touches": homeTeam[6].touches,
                    "home_" + homeTeam[6].position + "_lost": homeTeam[6].lost,
                    "home_" + homeTeam[6].position + "_rate": homeTeam[6].rate,
                    "home_" + homeTeam[6].position + "_fouls": homeTeam[6].fouls,
                    "home_" + homeTeam[6].position + "_blocks": homeTeam[6].blocks,
                    "home_" + homeTeam[7].position + "_name": homeTeam[7].name,
                    "home_" + homeTeam[7].position + "_assistence": homeTeam[7].assistence,
                    "home_" + homeTeam[7].position + "_won_contest": homeTeam[7].won_contest,
                    "home_" + homeTeam[7].position + "_tackles": homeTeam[7].tackles,
                    "home_" + homeTeam[7].position + "_goals": homeTeam[7].goals,
                    "home_" + homeTeam[7].position + "_red_card": homeTeam[7].red_card,
                    "home_" + homeTeam[7].position + "_yellow_card": homeTeam[7].yellow_card,
                    "home_" + homeTeam[7].position + "_touches": homeTeam[7].touches,
                    "home_" + homeTeam[7].position + "_lost": homeTeam[7].lost,
                    "home_" + homeTeam[7].position + "_rate": homeTeam[7].rate,
                    "home_" + homeTeam[7].position + "_fouls": homeTeam[7].fouls,
                    "home_" + homeTeam[7].position + "_blocks": homeTeam[7].blocks,
                    "home_" + homeTeam[8].position + "_name": homeTeam[8].name,
                    "home_" + homeTeam[8].position + "_assistence": homeTeam[8].assistence,
                    "home_" + homeTeam[8].position + "_won_contest": homeTeam[8].won_contest,
                    "home_" + homeTeam[8].position + "_tackles": homeTeam[8].tackles,
                    "home_" + homeTeam[8].position + "_goals": homeTeam[8].goals,
                    "home_" + homeTeam[8].position + "_red_card": homeTeam[8].red_card,
                    "home_" + homeTeam[8].position + "_yellow_card": homeTeam[8].yellow_card,
                    "home_" + homeTeam[8].position + "_touches": homeTeam[8].touches,
                    "home_" + homeTeam[8].position + "_lost": homeTeam[8].lost,
                    "home_" + homeTeam[8].position + "_rate": homeTeam[8].rate,
                    "home_" + homeTeam[8].position + "_fouls": homeTeam[8].fouls,
                    "home_" + homeTeam[8].position + "_blocks": homeTeam[8].blocks,
                    "home_" + homeTeam[9].position + "_name": homeTeam[9].name,
                    "home_" + homeTeam[9].position + "_assistence": homeTeam[9].assistence,
                    "home_" + homeTeam[9].position + "_won_contest": homeTeam[9].won_contest,
                    "home_" + homeTeam[9].position + "_tackles": homeTeam[9].tackles,
                    "home_" + homeTeam[9].position + "_goals": homeTeam[9].goals,
                    "home_" + homeTeam[9].position + "_red_card": homeTeam[9].red_card,
                    "home_" + homeTeam[9].position + "_yellow_card": homeTeam[9].yellow_card,
                    "home_" + homeTeam[9].position + "_touches": homeTeam[9].touches,
                    "home_" + homeTeam[9].position + "_lost": homeTeam[9].lost,
                    "home_" + homeTeam[9].position + "_rate": homeTeam[9].rate,
                    "home_" + homeTeam[9].position + "_fouls": homeTeam[9].fouls,
                    "home_" + homeTeam[9].position + "_blocks": homeTeam[9].blocks,
                    "home_" + homeTeam[10].position + "_name": homeTeam[10].name,
                    "home_" + homeTeam[10].position + "_assistence": homeTeam[10].assistence,
                    "home_" + homeTeam[10].position + "_won_contest": homeTeam[10].won_contest,
                    "home_" + homeTeam[10].position + "_tackles": homeTeam[10].tackles,
                    "home_" + homeTeam[10].position + "_goals": homeTeam[10].goals,
                    "home_" + homeTeam[10].position + "_red_card": homeTeam[10].red_card,
                    "home_" + homeTeam[10].position + "_yellow_card": homeTeam[10].yellow_card,
                    "home_" + homeTeam[10].position + "_touches": homeTeam[10].touches,
                    "home_" + homeTeam[10].position + "_lost": homeTeam[10].lost,
                    "home_" + homeTeam[10].position + "_rate": homeTeam[10].rate,
                    "home_" + homeTeam[10].position + "_fouls": homeTeam[10].fouls,
                    "home_" + homeTeam[10].position + "_blocks": homeTeam[10].blocks,
                    "home_" + homeTeam[11].position + "_name": homeTeam[11].name,
                    "home_" + homeTeam[11].position + "_assistence": homeTeam[11].assistence,
                    "home_" + homeTeam[11].position + "_won_contest": homeTeam[11].won_contest,
                    "home_" + homeTeam[11].position + "_tackles": homeTeam[11].tackles,
                    "home_" + homeTeam[11].position + "_goals": homeTeam[11].goals,
                    "home_" + homeTeam[11].position + "_red_card": homeTeam[11].red_card,
                    "home_" + homeTeam[11].position + "_yellow_card": homeTeam[11].yellow_card,
                    "home_" + homeTeam[11].position + "_touches": homeTeam[11].touches,
                    "home_" + homeTeam[11].position + "_lost": homeTeam[11].lost,
                    "home_" + homeTeam[11].position + "_rate": homeTeam[11].rate,
                    "home_" + homeTeam[11].position + "_fouls": homeTeam[11].fouls,
                    "home_" + homeTeam[11].position + "_blocks": homeTeam[11].blocks,
                    "home_" + homeTeam[12].position + "_name": homeTeam[12].name,
                    "home_" + homeTeam[12].position + "_assistence": homeTeam[12].assistence,
                    "home_" + homeTeam[12].position + "_won_contest": homeTeam[12].won_contest,
                    "home_" + homeTeam[12].position + "_tackles": homeTeam[12].tackles,
                    "home_" + homeTeam[12].position + "_goals": homeTeam[12].goals,
                    "home_" + homeTeam[12].position + "_red_card": homeTeam[12].red_card,
                    "home_" + homeTeam[12].position + "_yellow_card": homeTeam[12].yellow_card,
                    "home_" + homeTeam[12].position + "_touches": homeTeam[12].touches,
                    "home_" + homeTeam[12].position + "_lost": homeTeam[12].lost,
                    "home_" + homeTeam[12].position + "_rate": homeTeam[12].rate,
                    "home_" + homeTeam[12].position + "_fouls": homeTeam[12].fouls,
                    "home_" + homeTeam[12].position + "_blocks": homeTeam[12].blocks,
                    "home_" + homeTeam[13].position + "_name": homeTeam[13].name,
                    "home_" + homeTeam[13].position + "_assistence": homeTeam[13].assistence,
                    "home_" + homeTeam[13].position + "_won_contest": homeTeam[13].won_contest,
                    "home_" + homeTeam[13].position + "_tackles": homeTeam[13].tackles,
                    "home_" + homeTeam[13].position + "_goals": homeTeam[13].goals,
                    "home_" + homeTeam[13].position + "_red_card": homeTeam[13].red_card,
                    "home_" + homeTeam[13].position + "_yellow_card": homeTeam[13].yellow_card,
                    "home_" + homeTeam[13].position + "_touches": homeTeam[13].touches,
                    "home_" + homeTeam[13].position + "_lost": homeTeam[13].lost,
                    "home_" + homeTeam[13].position + "_rate": homeTeam[13].rate,
                    "home_" + homeTeam[13].position + "_fouls": homeTeam[13].fouls,
                    "home_" + homeTeam[13].position + "_blocks": homeTeam[13].blocks
                }
            }
            global_idpartidos = global_idpartidos + 1
            print(json.dumps(matcjob))

            with open('final.json') as f:
                data = json.load(f)

            data.update(matcjob)

            with open('final.json', 'w') as f:
                json.dump(data, f)
        return global_idpartidos

    def teamPlayerArray(datastats,idt,id):
        teamArray = ["","","","","","","","","","","","","",""]
        pointer =0
        # datastats[id][idt]['Player_stats']['Wojciech Szczesny'][player_details] or [Match_stats]
        for idtema in datastats[id][idt]['Player_stats']:
            jugador = Player()
            # para cada jugador

            try:
                jugador.name = datastats[id][idt]['Player_stats'][idtema]['player_details']['player_name']
            except:
                jugador.name = ""
            try:
                jugador.position = datastats[id][idt]['Player_stats'][idtema]['player_details']['player_position_info']
            except:
                jugador.position = ""
            try:
                jugador.rate = datastats[id][idt]['Player_stats'][idtema]['player_details']['player_rating']
            except:
                jugador.rate = ""
            try:
                jugador.blocks = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['saves']
            except:
                jugador.blocks = ""
            try:
                jugador.fouls = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['fouls']
            except:
                jugador.fouls = ""
            try:
                jugador.lost = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['aerial_lost']
            except:
                jugador.lost = ""
            try:
                jugador.passAccurate = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['accurate_pass']
            except:
                jugador.passAccurate = ""
            try:
                jugador.goals = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['goals']
            except:
                jugador.goals = ""
            try:
                jugador.tackles = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['total_tackle']
            except:
                jugador.tackles = ""
            try:
                jugador.touches = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['touches']
            except:
                jugador.touches = ""
            try:
                jugador.won_contest = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['won_contest']
            except:
                jugador.won_contest = ""
            try:
                jugador.yellow_card = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['yellow_card']
            except:
                jugador.yellow_card = ""
            try:
                jugador.red_card = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['red_card']
            except:
                jugador.red_card = ""
            try:
                jugador.assistence = datastats[id][idt]['Player_stats'][idtema]['Match_stats']['goal_assist']
            except:
                jugador.assistence = ""
            print(jugador.position)
            if (pointer<14):
                teamArray[pointer] = jugador
                pointer = pointer + 1
            else:
                break
        return teamArray

    def jsontocsv(directionjson):
        infile = open(directionjson, 'r')

        df = pd.read_json(infile)
        df.to_csv('../csvdatafile/season1/finalSeason.csv')
    main()
#execution
global_idpartidos =0
mainClass()