from flask import Flask, render_template, request

app = Flask(__name__)

def apply_stat_changes(base_value, percent_change):
    return base_value * (1 + percent_change / 100)

def calculate_dps(damage, cooldown):
    if cooldown == 0:
        return float('inf')
    return damage / cooldown

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            base_damage = float(request.form['base_damage'])
            base_range = float(request.form['base_range'])
            base_cooldown = float(request.form['base_cooldown'])

            damage_percent_change = float(request.form['damage_percent_change'])
            range_percent_change = float(request.form['range_percent_change'])
            cooldown_percent_change = float(request.form['cooldown_percent_change'])

            final_damage = apply_stat_changes(base_damage, damage_percent_change)
            final_range = apply_stat_changes(base_range, range_percent_change)
            final_cooldown = apply_stat_changes(base_cooldown, cooldown_percent_change)
            dps = calculate_dps(final_damage, final_cooldown)

            return render_template('index.html', 
                                   final_damage=f"{final_damage:.2f}", 
                                   final_range=f"{final_range:.2f}", 
                                   final_cooldown=f"{final_cooldown:.2f}", 
                                   dps=f"{dps:.2f}")
        except ValueError:
            return render_template('index.html', error="Invalid input. Please enter numbers only.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
