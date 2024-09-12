import matplotlib.pyplot as plt
from transactions.models import SellItem
from django.utils import timezone
from datetime import datetime, timedelta
from typing import Literal
import pandas as pd
import seaborn as sns
import io, urllib, base64, pytz

import matplotlib
matplotlib.use('Agg')

class PLOT_DATA:
    def __init__(self, tx_count, transaction_objects) -> None:
        self.now = timezone.now()
        self.year_now = datetime.now().year
        self.day_ago = self.now - timedelta(days=1)
        self.transactions = transaction_objects

        if tx_count != 0:
            self.day_revenue = [
                        {
                            'Revenue': x.total_price,
                            'date_transaction': x.date_transaction
                        } for x in self.transactions if self.day_ago <= x.date_transaction <= self.now
                    ]


            self.all_revenue = [
                {
                    'Revenue': x.total_price,
                    'date_transaction': x.date_transaction
                } for x in self.transactions
            ]

            self.quarter_revenue = [
                {
                    'Revenue': sum([float(x.total_price) for x in self.transactions 
                                if x.date_transaction >= timezone.make_aware(datetime(self.year_now, 1, 1)) 
                                and x.date_transaction <= timezone.make_aware(datetime(self.year_now, 3, 31))]),
                    'date_transaction': 'First Quarter'
                },
                {
                    'Revenue': sum([float(x.total_price) for x in self.transactions 
                                if x.date_transaction >= timezone.make_aware(datetime(self.year_now, 4, 1)) 
                                and x.date_transaction <= timezone.make_aware(datetime(self.year_now, 6, 30))]),
                    'date_transaction': 'Second Quarter'
                },
                {
                    'Revenue': sum([float(x.total_price) for x in self.transactions 
                                if x.date_transaction >= timezone.make_aware(datetime(self.year_now, 7, 1)) 
                                and x.date_transaction <= timezone.make_aware(datetime(self.year_now, 9, 30))]),
                    'date_transaction': 'Third Quarter'
                },
                {
                    'Revenue': sum([float(x.total_price) for x in self.transactions 
                                if x.date_transaction >= timezone.make_aware(datetime(self.year_now, 10, 1)) 
                                and x.date_transaction <= timezone.make_aware(datetime(self.year_now, 12, 31))]),
                    'date_transaction': 'Fourth Quarter'
                }
            ]


            self.day_margin = [
                        {
                            'Profit': x.total_margin,
                            'date_transaction': x.date_transaction
                        } for x in self.transactions if self.day_ago <= x.date_transaction <= self.now
                    ]

            self.all_margin = [
                {
                    'Profit': x.total_margin,
                    'date_transaction': x.date_transaction
                } for x in self.transactions
            ]

            self.quarter_margin = [
                {
                    'Profit': sum([float(x.total_margin) for x in self.transactions 
                                if x.date_transaction >= timezone.make_aware(datetime(self.year_now, 1, 1)) 
                                and x.date_transaction <= timezone.make_aware(datetime(self.year_now, 3, 31))]),
                    'date_transaction': 'First Quarter'
                },
                {
                    'Profit': sum([float(x.total_margin) for x in self.transactions 
                                if x.date_transaction >= timezone.make_aware(datetime(self.year_now, 4, 1)) 
                                and x.date_transaction <= timezone.make_aware(datetime(self.year_now, 6, 30))]),
                    'date_transaction': 'Second Quarter'
                },
                {
                    'Profit': sum([float(x.total_margin) for x in self.transactions 
                                if x.date_transaction >= timezone.make_aware(datetime(self.year_now, 7, 1)) 
                                and x.date_transaction <= timezone.make_aware(datetime(self.year_now, 9, 30))]),
                    'date_transaction': 'Third Quarter'
                },
                {
                    'Profit': sum([float(x.total_margin) for x in self.transactions 
                                if x.date_transaction >= timezone.make_aware(datetime(self.year_now, 10, 1)) 
                                and x.date_transaction <= timezone.make_aware(datetime(self.year_now, 12, 31))]),
                    'date_transaction': 'Fourth Quarter'
                }
            ]

        else:
            self.day_margin, self.all_margin, self.quarter_margin = None
            self.day_revenue, self.all_revenue, self.quarter_revenue = None

    def _bargraph(self, data, ddtype: str, dfclass: Literal['daily','all','quarter']):
        # Check if DataFrame is empty
        if data is not None and not data.empty and ddtype:
            fig, ax = plt.subplots(figsize=(8,5))
            
            
            if dfclass == 'daily':
                if pd.api.types.is_datetime64_any_dtype(data['date_transaction']):
                    # data['date_transaction'] = pd.to_datetime(data['date_transaction'])
                    # x_value = pd.date_range(start=self.day_ago+timedelta(hours=8), end=self.now+timedelta(hours=8), freq='H')
                    # x_label = x_value.strftime('%b %d, %I:%M%p')
                    # ax.set_xticks(x_value)
                    # ax.set_xlim(x_value.min(), x_value.max())
                    sns.barplot(data, x="date_transaction", y=ddtype,
                                linewidth=3, edgecolor="black", facecolor=(235/255,42/255,177/255)
                                ,ax=ax)

                    ax.set_xticklabels(data['date_transaction'].dt.strftime('%b %d, %I:%M%p'))
                    ax.set_xlabel('')
                    ax.set_title('Daily Data', fontsize=14)

            elif dfclass == 'all':
                if pd.api.types.is_datetime64_any_dtype(data['date_transaction']):
                    data['date_transaction'] = data['date_transaction'].dt.strftime('%b %d, %I:%M%p')
                    sns.barplot(data, x="date_transaction", y=ddtype,
                                linewidth=3, edgecolor="black", facecolor=(70/255,12/255,171/255)
                                ,ax=ax, errorbar=None)
                    ax.set_title('Overall Data', fontsize=14)
                    ax.set_xlabel('')

            elif dfclass == 'quarter':
                sns.barplot(data, x="date_transaction", y=ddtype,
                                linewidth=3, edgecolor="black", facecolor=(48/255,200/255,217/255)
                                ,ax=ax, errorbar=None)
                ax.set_xlabel('')
                ax.set_title('Quarter Data', fontsize=14)


            ax.tick_params(which='major', axis='x', labelrotation=90, labelsize=7)
            ax.set_ylabel('Amount')
            buffer = io.BytesIO()
            plt.tight_layout()
            plt.subplots_adjust(hspace=0.15)
            plt.savefig(buffer, format='png')
            plt.close()
            buffer.seek(0)

            # Encode the image to a base64 string
            image_png = buffer.getvalue()
            graph = base64.b64encode(image_png).decode('utf-8')
            buffer.close()

            return graph
        else:
            return None  # Return None if the DataFrame is empty


    def return_df(self, datatype:Literal['revenue','profit']):
        '''
        Return the pandas.DataFrame form of all dataset. All output was 
        returned in DAY, ALL, QUARTERLY arrangement.
        '''

        df1, df2, df3 =  pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

        if datatype == 'revenue':
            if self.day_revenue:  
                df1 = pd.DataFrame(self.day_revenue)
            if self.all_revenue:  
                df2 = pd.DataFrame(self.all_revenue)
            if self.quarter_revenue:  
                df3 = pd.DataFrame(self.quarter_revenue)
        elif datatype == 'profit':
            if self.day_margin: 
                df1 = pd.DataFrame(self.day_margin)
            if self.all_margin: 
                df2 = pd.DataFrame(self.all_margin)
            if self.quarter_margin:  
                df3 = pd.DataFrame(self.quarter_margin)

        return df1,df2,df3

    def get_figs(self, datatype: Literal['revenue', 'profit']):
        if datatype == 'revenue':
            day_rev, all_rev, quarter_rev = self.return_df(datatype=datatype)
            return (
                self._bargraph(day_rev, 'Revenue', 'daily'),
                self._bargraph(all_rev, 'Revenue', 'all'),
                self._bargraph(quarter_rev, 'Revenue', 'quarter')
            )
        elif datatype == 'profit':
            day_prof, all_prof, quarter_prof = self.return_df(datatype=datatype)
            return (
                self._bargraph(day_prof, 'Profit', 'daily'),
                self._bargraph(all_prof, 'Profit', 'all'),
                self._bargraph(quarter_prof, 'Profit', 'quarter')
            )



    