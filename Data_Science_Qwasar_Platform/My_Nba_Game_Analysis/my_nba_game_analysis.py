def print_nba_game_stats(data_dict):
    print("    Players  FG  FGA  FG%  3P  3PA  3P%  FT  FTA  FT%  ORB  DRB  TRB  AST  STL  BLK  TOV  PF  PTS")
    t_fg = t_fga = t_fg_p = t_p = t_pa = t_p_p = t_ft = t_fta = t_ft_p = t_orb = t_drb = t_trb = t_ast = t_stl = t_blk = t_tov = t_pf = t_pts = 0
    for i in range(len(data_dict["players_data"])):
        print(data_dict["players_data"][i]["player_name"] + "   " + str(
            data_dict["players_data"][i]["FG"]) + "    " + str(data_dict["players_data"][i]["FGA"]) + "    " + str(
            data_dict["players_data"][i]["FG%"]) + "    " + str(data_dict["players_data"][i]["3P"]) + "   " + str(
            data_dict["players_data"][i]["3PA"]) + "    " + str(data_dict["players_data"][i]["3P%"]) + "    " + str(
            data_dict["players_data"][i]["FT"]) + "   " + str(data_dict["players_data"][i]["FTA"]) + "    " + str(
            data_dict["players_data"][i]["FT%"]) + "    " + str(data_dict["players_data"][i]["ORB"]) + "    " + str(
            data_dict["players_data"][i]["DRB"]) + "    " + str(data_dict["players_data"][i]["TRB"]) + "    " + str(
            data_dict["players_data"][i]["AST"]) + "    " + str(data_dict["players_data"][i]["STL"]) + "    " + str(
            data_dict["players_data"][i]["BLK"]) + "    " + str(data_dict["players_data"][i]["TOV"]) + "    " + str(
            data_dict["players_data"][i]["PF"]) + "   " + str(data_dict["players_data"][i]["PTS"]))
        t_fg += data_dict["players_data"][i]["FG"]
        t_fga += data_dict["players_data"][i]["FGA"]
        t_p += data_dict["players_data"][i]["3P"]
        t_pa += data_dict["players_data"][i]["3PA"]
        t_ft += data_dict["players_data"][i]["FT"]
        t_fta += data_dict["players_data"][i]["FTA"]
        t_orb += data_dict["players_data"][i]["ORB"]
        t_drb += data_dict["players_data"][i]["DRB"]
        t_trb += data_dict["players_data"][i]["TRB"]
        t_ast += data_dict["players_data"][i]["AST"]
        t_stl += data_dict["players_data"][i]["STL"]
        t_blk += data_dict["players_data"][i]["BLK"]
        t_tov += data_dict["players_data"][i]["TOV"]
        t_pf += data_dict["players_data"][i]["PF"]
        t_pts += data_dict["players_data"][i]["PTS"]
    if t_fga != 0:
        t_fg_p = round(t_fg / t_fga, 3)
    if t_pa != 0:
        t_p_p = round(t_p / t_pa, 3)
    if t_fta != 0:
        t_ft_p = round(t_ft / t_fta, 3)
    print(
        "Team Totals {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}\n".format(
            t_fg, t_fga, t_fg_p, t_p, t_pa, t_p_p, t_ft, t_fta, t_ft_p, t_orb, t_drb, t_trb, t_ast, t_stl, t_blk, t_tov,
            t_pf, t_pts))


def add_data(data, ah_list):
    temp_list = []
    for sr in data:
        temp_list.append(
            {"player_name": sr["player_name"], "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0,
             "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0,
             "PTS": 0})
    for i in range(len(temp_list)):
        if temp_list[i] not in temp_list[i + 1:]:
            ah_list.append(temp_list[i])
    for w in ah_list:
        for s in data:
            if s["player_name"] == w["player_name"]:
                w["FG"] += s["FG"]
                w["FGA"] += s["FGA"]
                w["3P"] += s["3P"]
                w["3PA"] += s["3PA"]
                w["FT"] += s["FT"]
                w["FTA"] += s["FTA"]
                w["ORB"] += s["ORB"]
                w["DRB"] += s["DRB"]
                w["TRB"] += s["TRB"]
                w["TOV"] += s["TOV"]
                w["PTS"] += s["PTS"]
    for q in ah_list:
        if q["FGA"] != 0:
            q["FG%"] = round(q["FG"] / q["FGA"], 3)
        if q["3PA"] != 0:
            q["3P%"] = round(q["3P"] / q["3PA"], 3)
        if q["FTA"] != 0:
            q["FT%"] = round(q["FT"] / q["FTA"], 3)
    return ah_list


def count_data(players, ah_list, cur_tname, a_tname):
    import re
    for f in range(len(players)):
        nmatch = re.search(r'[A-Z]. [A-Z]\w+\)', players[f][7])
        _match = re.search(r'[A-Z]. [A-Z]\w+', players[f][7])
        ast1 = re.search(r'assist', players[f][7])
        blk1 = re.search(r'block', players[f][7])
        stl1 = re.search(r'steal', players[f][7])
        pf1 = re.search(r'Personal foul by', players[f][7])
        sh_f = re.search(r'Shooting foul by', players[f][7])
        of_f = re.search(r'Offensive foul by', players[f][7])
        l_f = re.search(r'Clear path foul by', players[f][7])
        if _match != None:
            if sh_f != None or l_f != None or of_f != None or pf1 != None:
                for h in ah_list:
                    if _match.group() == h["player_name"]:
                        h["PF"] += 1
        if blk1 != None and players[f][2] == a_tname and nmatch != None:
            m = re.search(r'[A-Z]. [A-Z]\w+', nmatch.group())
            for h in ah_list:
                if m.group() == h["player_name"]:
                    h["BLK"] += 1
        if stl1 != None and players[f][2] == a_tname and nmatch != None:
            m = re.search(r'[A-Z]. [A-Z]\w+', nmatch.group())
            for h in ah_list:
                if m.group() == h["player_name"]:
                    h["STL"] += 1
        if ast1 != None and players[f][2] == cur_tname and nmatch != None:
            m = re.search(r'[A-Z]. [A-Z]\w+', nmatch.group())
            for h in ah_list:
                if m.group() == h["player_name"]:
                    h["AST"] += 1
    return ah_list


def analyse_nba_game(players):
    import re
    h_players_data = []
    a_players_data = []
    h_res_list = []
    a_res_list = []
    data_away = {"name": players[0][3], "players_data": a_res_list}
    data_home = {"name": players[0][4], "players_data": h_res_list}
    res = {
        "home_team": data_home,
        "away_team": data_away
    }
    d = fg = fga = p = pa = ft = fta = orb = drb = trb = ast = stl = blk = tov = pf = pts = 0
    for c in range(len(players)):
        match = re.search(r'[A-Z]. [A-Z]\w+', players[c][7])
        p2 = re.search(r'makes 2-pt', players[c][7])
        pa2 = re.search(r'2-pt', players[c][7])
        p3 = re.search(r'makes 3-pt', players[c][7])
        pa3 = re.search(r'3-pt', players[c][7])
        ft1 = re.search(r'misses free throw', players[c][7])
        fta1 = re.search(r'free throw', players[c][7])
        orb1 = re.search(r'Offensive rebound', players[c][7])
        drb1 = re.search(r'Defensive rebound', players[c][7])
        tov1 = re.search(r'Turnover', players[c][7])
        pf1 = re.search(r'Personal foul', players[c][7])
        foul = re.search(r'foul by', players[c][7])
        if match != None:
            if p2 != None or p3 != None:
                fg = fg + 1
            if p2 != None:
                pts = pts + 2
            if pa2 != None or pa3 != None:
                fga = fga + 1
            if p3 != None:
                p = p + 1
                pts = pts + 3
            if pa3 != None:
                pa = pa + 1
            if fta1 != None and ft1 == None:
                ft = ft + 1
                pts += 1
            if fta1 != None:
                fta = fta + 1
            if orb1 != None:
                orb = orb + 1
            if drb1 != None:
                drb = drb + 1
            if orb1 != None or drb1 != None:
                trb = trb + 1
            if tov1 != None:
                tov = tov + 1
            if pf1 != None and foul == None:
                pf = pf + 1
            if players[c][2] == players[0][3]:
                if foul == None:
                    a_players_data.append(
                        {"player_name": match.group(), "FG": fg, "FGA": fga, "FG%": d, "3P": p, "3PA": pa, "3P%": d,
                         "FT": ft, "FTA": fta, "FT%": d, "ORB": orb, "DRB": drb, "TRB": trb, "AST": ast, "STL": stl,
                         "BLK": blk, "TOV": tov, "PF": pf, "PTS": pts})
            if players[c][2] == players[0][4]:
                if foul == None:
                    h_players_data.append(
                        {"player_name": match.group(), "FG": fg, "FGA": fga, "FG%": d, "3P": p, "3PA": pa, "3P%": d,
                         "FT": ft, "FTA": fta, "FT%": d, "ORB": orb, "DRB": drb, "TRB": trb, "AST": ast, "STL": stl,
                         "BLK": blk, "TOV": tov, "PF": pf, "PTS": pts})
            fg = fga = p = pa = ft = fta = orb = drb = trb = tov = pf = pts = 0

    h_res_list = add_data(h_players_data, h_res_list)
    a_res_list = add_data(a_players_data, a_res_list)

    h_res_list = count_data(players, h_res_list, players[0][4], players[0][3])
    a_res_list = count_data(players, a_res_list, players[0][3], players[0][4])
    # print(res)
    print_nba_game_stats(data_home)
    print_nba_game_stats(data_away)
    return res


my_join = ' '
with open('nba_game_warriors.txt', 'r') as game:
    my_join = my_join.join(game)
output = []
players = my_join.split('\n')
for row in players:
    if row != "":
        output.append(row.split("|"))
analyse_nba_game(output)
