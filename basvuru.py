from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

basvurular = []

@app.route('/')
def ana_sayfa():
    return render_template('basvuru_formu.html')

@app.route('/basvuru_gonder', methods=['POST'])
def basvuru_gonder():
    ad = request.form['ad']
    soyad = request.form['soyad']
    email = request.form['email']
    pozisyon = request.form['pozisyon']

    basvuru = {
        'ad': ad,
        'soyad': soyad,
        'email': email,
        'pozisyon': pozisyon
    }

    basvurular.append(basvuru)
    return redirect(url_for('basvuru_listesi'))

@app.route('/basvurular')
def basvuru_listesi():
    return render_template('basvuru_listesi.html', basvurular=basvurular)

if __name__ == '__main__':
    app.run(debug=True)
