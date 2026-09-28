#pip install argostranslate

#import argostranslate.package
#import argostranslate.translate

#from_code = "en"
#to_code = "es"





from argostranslate import package, translate

# Download package between English and French
package.install_from_path('en_fr.argosmodel')

installed_languages = translate.get_installed_languages()
translation = installed_languages[0].get_translation(installed_languages[1])
print(translation.translate("Hello"))  # Works offline!